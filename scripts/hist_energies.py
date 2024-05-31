import json
import glob
import argparse
import h5py
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description = "plot energy distribution")
parser.add_argument("sim_dir",
                    nargs = "?",
                    metavar = "sim file directory",
                    default = "/CECI/proj/rnog/simulated_station_data_sets/data",
                    help = "root directory of all simulation files")
args = parser.parse_args()

def read_energies(sim_paths : np.ndarray)->np.ndarray:
    energies = []
    for sim_path in sim_paths:
        file = h5py.File(sim_path, "r")
        energies += file["energies"]
    energies = np.array(energies)
    return energies

def plot_hist(values : np.ndarray) -> None:
    fig, ax = plt.subplots()

    ax.hist(values, rwidth = 0.9)
    ax.grid()
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Energy / eV", size = "large")
    ax.set_ylabel("counts", size = "large")
    fig.savefig("../figures/test")
    return

if __name__ == "__main__":
    sim_paths = glob.glob(f"{args.sim_dir}/**/*.hdf5", recursive = True)
    energies = read_energies(sim_paths)
    plot_hist(energies)
