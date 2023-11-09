import matplotlib.pyplot as plt
import numpy as np

# there's a few critical thoughts
# which I had left out on the original diagram.
# for example, I assumed things would continue
# at the current speed, rather than at the ideal speed.

years = [ 2020,  2025,  2030,   2035,   2040]
# in TWh
solar = [  854,  8540, 85400, 170000, 220000]
wind  = [ 1594,  3744, 10076,  27199,  60000]
water = [ 4359,  4359,  4359,   3000,   2000]
plant = [12185, 12185, 12185,  12185,  20000]
gas   = [38603, 38603, 30000,  13000,      0]
oil   = [48610, 48610, 30000,  13000,      0]
coal  = [42233, 42233, 30000,  13000,      0]

gsmt = [146000,156500,200000, 250000, 300000]

nclr  = [ 2679,  2679,  2679,  2679,  1300,      0,      0]

# layout bugfix
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.title("World Energy outlook '40 (in TWh)")
ax.stackplot(years,
	[
		coal, oil, gas,
		plant,
		water, wind, solar,
	],
	colors = (
		"#533", "#733", "#933",
		"#3b3",
		"#3bb", "#33b", "#11f",
	),
	labels = (
		"Coal", "Oil", "Gas",
		"Renewable Biomass",
		"Water power", "Wind", "Solar"
	)
)

#plt.legend()
# fix to reverse the order of the legend:
# https://stackoverflow.com/questions/34576059/reverse-the-order-of-a-legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1])

# only show integers on the x-axis
# https://stackoverflow.com/questions/12050393/how-to-force-the-y-axis-to-only-use-integers
ax.xaxis.get_major_locator().set_params(integer = True)

#plt.show()
plt.savefig("plot-2.png", dpi=400)
