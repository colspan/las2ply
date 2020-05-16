# las2ply

## Setup

```bash
pip install git+https://github.com/colspan/las2ply
```

## Usage

### Basic

```bash
las2ply /path/to/las/*.las output.ply
```

### With reducing points byskipping with static rate

```bash
las2ply /path/to/las/*.las output.ply  --skip-rate 0.80
```

### With voxel sampling

```bash
las2ply /path/to/las/*.las output.ply  --voxel-size 0.10
```

