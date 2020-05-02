from ipywidgets import interact
import ipywidgets as widgets

def f(x):
    return x**2

interact(f, x=10.);