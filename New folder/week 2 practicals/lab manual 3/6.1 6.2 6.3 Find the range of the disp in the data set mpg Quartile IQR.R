# i) Find the range of disp in the "mpg" dataset
range_disp <- range(mpg$displ)
range_disp

# ii) Find the quartiles of disp in the "mpg" dataset
quartiles_disp <- quantile(mpg$displ)
quartiles_disp

# iii) Find the interquartile range (IQR) of disp in the "mpg" dataset
iqr_disp <- IQR(mpg$displ)
iqr_disp
