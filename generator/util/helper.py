def log_settings(args, logger):
    logger.info(f"GPU: {args.gpu_ids}")
    logger.info(f"Model: {args.model}")
    logger.info(f"Generator: {args.netG}")
    if args.model == 'pix2pix':
        logger.info(f"Discriminator: {args.netD}")
        logger.info(f"GAN objective: {args.gan_mode}")
    elif args.model == 'pix2pixHD':
        logger.info(f"Number of local enhancers: {args.n_local_enhancers}")
        logger.info(f"Number of discriminators: {args.num_D}")
    logger.info(f"Normalization: {args.norm}")
    logger.info(f"Weight initialization: {args.init_type}")
    logger.info(f"Using dropout: {args.use_dropout}")
    logger.info(f"Batch size: {args.batch_size}")
    logger.info(f"Number of epochs: {args.n_epochs}")
    logger.info(f"Learning rate: {args.lr}")
    logger.info(f"Momentum: {args.beta1}")
    logger.info(f"Learning rate policy: {args.lr_policy}")
    logger.info(f"Number of epochs to fix lr: {args.lr_fix_epochs}")
    logger.info(f"Number of epochs to decay lr to 0: {args.lr_decay_epochs}")
    logger.info(f"Multiply lr by gamma every iterations: {args.lr_decay_iters}")
    logger.info(f"Number of training: {args.num_train}")
    logger.info(f"Number of evaluation: {args.num_eval}")