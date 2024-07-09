from pes_scan import pes_scan
geom = '''
    geometry noprint adjust
        zcoord
            bond  1 3   %f ci  constant
            bond  2 3   %f ccl  constant
        end
    end
'''
x0=3.000
y0=1.801
xmax=2.171
ymax=3.000
npts=7
xmin = x0 - (xmax-x0)/npts
ymin = y0 - (ymax-y0)/npts
results = pes_scan(geom, \
[xmin, ymin],
[xmax,  ymax],
npts, 'dft', task_optimize)
fp=open("pes2d.dat","w")
fp.write(f'# {npts} {npts}  \n')
for i in range(0,len(results)):
    fp.write(f'{results[i][0][0]} {results[i][0][1]}  {results[i][1]} \n')
fp.close()

