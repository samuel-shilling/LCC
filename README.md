A machine learning GRB Afteglow light curve classifier

# Capabilities
1. Identify flares

2. Estimate the morphological classifcation given the data

3. Interpolate and extrpolate missing data based on the classification for a given confidence level



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



# Data information

## Source
All data are publicly available in the Leicester Swift website (see references in Shilling et al. 2026; https://academic.oup.com/mnras/article/552/2/stag1589/8767814)

## Columns
- GRB is the name of each GRB
- Time,TimePos,TimeNeg are the times, positive, negative uncertainties in seconds in the observer frame
- Rate,RatePos,RateNeg are the count rates in counts per second and positive/negative uncertainties
- alpha_x, D_alpha_x are the slope of power-law segment x and the uncertainty
- break_x, D_break_x are the break times in seconds between each power-law segment