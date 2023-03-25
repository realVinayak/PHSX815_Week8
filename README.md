# PHSX815_Week8
This is a python implementation of Dr. Rogan's code at https://github.com/crogan/PHSX815_Week8/blob/master/macros/Neyman.C. <br/>
To run the code, type `python3 driver.py`. 
The code will simulate `N_exp = 10000` experiments with `N_meas = 5` measurements per an experiment.
The true distribution is Gaussian distribution with true mean ranging from `MIN_MU = -10` to `MAX_MU = 10`.
The standard deviation is chosen to be `STD_DEV = 2`. These constants can be changed in `driver.py` file.<br/>
The output will plot a histogram of measurement mean verses the true mean. The plot is saved at `plot.png`
