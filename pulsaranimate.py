import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from astropy.io import ascii

#Fetching data from the Database
url1 = 'http://rian.kharkov.ua/decameter/EPN/epndb/J0006+1834/cn95.epn.asc'
psr1 = ascii.read(url1,names=('Time','Data'),data_start=2)

#Initializing the animation parameters
Writer = animation.writers['ffmpeg']
writer = Writer( fps = 10, metadata = dict(artist = 'Me'), bitrate = 1800)

#Defining the plotting parameters
fig=plt.figure( figsize = (10, 10) )
plt.style.use('dark_background')
plt.title('Pulsar Profile of J0006+1834', fontsize = 20)
plt.xlim(0,0.7)
plt.ylim(-0.2,1)
plt.xlabel('Time (sec)',fontsize=20)
plt.ylabel('Intensity (arbritary units)', fontsize=20)

#Animate function to plot the graph as an animation
def animate(i):
    plt.plot(psr1['Time'][:int(i+1)], psr1['Data'][:int(i+1)],'r')
    plt.legend(['Integrated Profile'])

#Creating and saving the animation    
ani = matplotlib.animation.FuncAnimation(fig, animate, frames=500)
ani.save('Pulsar.mp4', writer = writer)
