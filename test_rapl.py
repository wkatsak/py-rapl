import time
import rapl

if __name__ == "__main__":
	s1 = rapl.RAPLMonitor.sample()
	time.sleep(5)
	s2 = rapl.RAPLMonitor.sample()

	diff = s2 - s1

	#print "S1", s1.energy("package-0", "core", rapl.WATT_HOURS)
	#s1.dump()

	#print "S2", s2.energy("package-0", "core", rapl.WATT_HOURS)
	#s2.dump()

	for d in diff.domains:
		domain = diff.domains[d]
		power = diff.average_power(package=domain.name)
		print("%s - %0.2f W" % (domain.name, power))

		for sd in domain.subdomains:
			subdomain = domain.subdomains[sd]
			power = diff.average_power(package=domain.name, domain=subdomain.name)
			print("\t%s - %0.2f W" % (subdomain.name, power))


	#print "Diff", diff.energy("package-0", "core", rapl.WATT_HOURS), diff.average_power("package-0", "core")
	#diff.dump()
