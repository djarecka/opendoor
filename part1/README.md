This is a solution for part1.

==========================

- The code can be run (data not included):

> python full_model.py

- I've built separate smaller models for:
   - lat/lon
   - numbers of bedrooms, baths and exterior stories
   - living area
   - list price
   - categorical features included in pool and dwelling type

- Building smaller models and creating a pipeline allows me to test importance of various variables
in a very easy way.

- I've started from a simple linear regression model with l2 regularization included sklearn package.

- Including all smaller models give a score (R^2 metric) gives around 0.4 and 0.08 without including list price. This can be significantly improved when I remove the category model (0.98 and 0.6 respectively).

- First things to improve:

   - building a better categorical model
   - applying CV
   - testing different models (at least RidgeCV)
   - adding another features
 
