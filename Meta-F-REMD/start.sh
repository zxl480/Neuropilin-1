rm temp
mkdir temp
cd /home/lzl/Desktop/NRPSample/md0
rm COLVAR* HILL* \#* bck* init.gro
rm -r CV
rm -r MD
mkdir CV
mkdir MD

gmx grompp -f md.mdp -c nvt.gro -t nvt.cpt  -p topol.top -o init.tpr
#nohup gmx mdrun -deffnm init -gpu_id 0   -pin on -pinoffset 0  -nt 8  -nb gpu -pme gpu -bonded gpu  -pmefft gpu &
#nohup gmx mdrun -deffnm init -gpu_id 0 -ntomp 10 &
nohup gmx mdrun -deffnm init -ntmpi 1 -ntomp 3 -pin on -pinoffset 0 -pinstride 1 -gpu_id 0 -nb gpu -pme gpu -bonded gpu -pmefft gpu &

cd /home/lzl/Desktop/NRPSample/md1
rm COLVAR* HILL* \#* bck* init.gro
rm -r CV
rm -r MD
mkdir CV
mkdir MD
gmx grompp -f md.mdp -c nvt.gro -t nvt.cpt  -p topol.top -o init.tpr
#nohup gmx mdrun -deffnm init -gpu_id 1 -ntomp 10 &
nohup gmx mdrun -deffnm init -ntmpi 1 -ntomp 3 -pin on -pinoffset 10 -pinstride 1 -gpu_id 1 -nb gpu -pme gpu -bonded gpu -pmefft gpu &

cd /home/lzl/Desktop/NRPSample/md2
rm COLVAR* HILL* \#* bck* init.gro
rm -r CV
rm -r MD
mkdir CV
mkdir MD
gmx grompp -f md.mdp -c nvt.gro -t nvt.cpt  -p topol.top -o init.tpr
#nohup gmx mdrun -deffnm init -gpu_id 3 -ntomp 10 &
nohup gmx mdrun -deffnm init -ntmpi 1 -ntomp 3 -pin on -pinoffset 20 -pinstride 1 -gpu_id 2 -nb gpu -pme gpu -bonded gpu -pmefft gpu &

wait

cd /home/lzl/Desktop/NRPSample/md0
rm  init.cpt init.xtc init.trr  init.tpr init.edr init_*
cd /home/lzl/Desktop/NRPSample/md1
rm  init.cpt init.xtc init.trr  init.tpr init.edr init_*
cd /home/lzl/Desktop/NRPSample/md2
rm  init.cpt init.xtc init.trr  init.tpr init.edr init_*

cd /home/lzl/Desktop/NRPSample
rm -r SELECT
mkdir SELECT
