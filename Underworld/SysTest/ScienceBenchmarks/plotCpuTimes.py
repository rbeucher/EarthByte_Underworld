#! /usr/bin/env python

import sys, math
from credo.modelresult import ModelResult

def getPerStepCPU_Times(freqOutput):
    freqOutput.populateFromFile()
    assert 'CPU_Time' in freqOutput.headers
    cpuIncTimes = freqOutput.getValuesArray('CPU_Time')
    cpuTimes = [0] * len(cpuIncTimes)
    cpuTimes[0] = cpuIncTimes[0]
    for ii, t in enumerate(cpuIncTimes[1:]):
        cpuTimes[ii+1] = t - cpuIncTimes[ii]
    return cpuTimes    

def plot(cpuTimes, modelDir):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.plot(cpuTimes)
    plt.xlabel("timestep")
    plt.ylim(0, math.ceil(max(cpuTimes)*10)/10.0)
    plt.ylabel("Time (sec)")
    plt.title("CPU Time per timestep\n(%s)" % modelDir)
    plt.show()

if __name__ == "__main__":
    try:
        outputPath = sys.argv[1]
    except:
        print "Bad input arguments - pass output path to model result."
        raise
    mRes = ModelResult("plotModel", outputPath)
    mRes.readFrequentOutput()
    fo = mRes.freqOutput
    cpuTimes = getPerStepCPU_Times(fo)
    plot(cpuTimes, outputPath)
