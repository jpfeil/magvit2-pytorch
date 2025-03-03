from setuptools import setup, find_packages

exec(open('magvit2_pytorch/version.py').read())

setup(
  name = 'magvit2-pytorch',
  packages = find_packages(),
  version = __version__,
  license='MIT',
  description = 'MagViT2 - Pytorch',
  long_description_content_type = 'text/markdown',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/magvit2-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformer',
    'attention mechanisms',
    'generative video model'
  ],
  install_requires=[
    'accelerate>=0.24.0',
    'beartype',
    'einops>=0.7.0',
    'ema-pytorch>=0.2.4',
    'gateloop-transformer>=0.0.25',
    'kornia',
    'opencv-python',
    'pillow',
    'numpy',
    'vector-quantize-pytorch>=1.10.8',
    'torch',
    'torchvision',
    'x-transformers'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
