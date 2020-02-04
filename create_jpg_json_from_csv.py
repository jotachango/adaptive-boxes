
import sys

from adabox.plot_tools import plot_rectangles
from adabox.tools import load_from_json, Rectangle, save_to_json
import numpy as np
import matplotlib.pyplot as plt
plt.ioff()


if len(sys.argv) < 3:
    print('ERROR args. Needed \n[1]in_path(.json) \n[2]out_path(.jpg)')
    sys.exit()

in_path = str(sys.argv[1])      # .json
out_path = str(sys.argv[2])     # .jpg


data = np.loadtxt(in_path, delimiter=',', dtype="int")
sep_value = 1


recs = []
for jd in data:
    recs.append(Rectangle(jd[0], jd[1], jd[2], jd[3]))


plot_rectangles(recs, sep_value)
plt.savefig(out_path + '.jpg', dpi=4000)

save_to_json(out_path + '.json', data, sep_value)
