# py-rapl: a very simple library to sample RAPL counters via powercap/sysfs interface

## Introduction

`py-rapl` is a very simple library that supports sampling the
[RAPL](https://01.org/blogs/2014/running-average-power-limit-%E2%80%93-rapl), or *Running Average Power Limit*
energy counters that are provided by most, if not all modern Intel CPUs.

## Usage
    import rapl

    s1 = rapl.RAPLMonitor.sample()
	# Some work that you want to measure.
	s2 = rapl.RAPLMonitor.sample()

    # Take the difference of the samples
	diff = s2 - s1

    # Print the difference in microjoules
	print(diff.energy("package-0", "core", rapl.UJOULES))

	# Print the average power
	print(diff.average_power("package-0", "core"))
