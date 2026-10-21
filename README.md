A machine learning GRB Afteglow light curve classifier

# Capabilities
1. Identify flares

2. Fit light curves (excluding flares) with a broken power-law

3. Estimate the morphological classifcation given the data for a given confidence level

4. Interpolate and extrpolate missing data based on the classification for a given confidence level



# Setup history
1. Create venv
```bash
conda create --name LCC python=3.12
conda activate LCC
```

2. Select LCC as the .vscode default env
cmd + shift + P 
select interpreter
LCC

3. Install all dependencies via pip then save to requirements
pip freeze > requirements.txt