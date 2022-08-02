import logging as log


log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('data_layer.log'),
                    log.StreamHandler()
                ])

# log.debug('DEBUG LEVEL MESSAGE')
# log.info('INFO LEVEL MESSAGE')
# log.warning('WARNING LEVEL MESSAGE')
# log.error('ERROR LEVEL MESSAGE')
# log.critical('CRITICAL LEVEL MESSAGE')
