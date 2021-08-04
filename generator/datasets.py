import os
from glob import glob
from torch.utils import data
from PIL import Image
from torchvision import transforms

class CustomDataset(data.Dataset):
    def __init__(self, folder, num_data):
        super().__init__()

        self.edges_and_images = list()

        assert len(folder)
        for data_folder in folder:
            assert os.path.exists(data_folder)
            components = os.path.normpath(data_folder).split(os.sep)

            if any([f in ["edges2shoes", "edges2handbags"] for f in components]):
                self.edges_and_images += \
                    [(path, self._getABImageData) for path in sorted(glob(os.path.join(data_folder, "*.jpg")))]
            
            elif any([f in ["lhq_256", "kaggle_landscape"] for f in components]):
                assert sorted(glob(os.path.join(data_folder, "*"))) == ["edges", "images"]
                self.edges_and_images += \
                    [((edges, image), self._getImageEdgeData) for edges, image in zip(
                        sorted(glob(os.path.join(data_folder, "edges", "*.jpg"))),
                        sorted(glob(os.path.join(data_folder, "images", "*.png")))
                    )]

        if num_data != -1:
            self.edges_and_images = self.edges_and_images[:num_data]
        
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])

    def __len__(self):
        return len(self.edges_and_images)

    def __getitem__(self, index):
        path, process_fn = self.edges_and_images[index]
        return process_fn(path)

    def _getABImageData(self, path):
        # read image from path
        AB = Image.open(path).convert('RGB')
        # split AB image into A and B
        w, h = AB.size
        w2 = int(w / 2)
        edge = AB.crop((0, 0, w2, h))
        image = AB.crop((w2, 0, w, h))
        return {
            'A': self.transform(edge), 
            'B': self.transform(image), 
            'A_paths': path, 
            'B_paths': path
        }

    def _getImageEdgeData(self, path):
        return