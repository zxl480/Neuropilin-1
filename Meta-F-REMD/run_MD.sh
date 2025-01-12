for((j=11;j<=100;j++));
do 
   cd path_to_MD/md0
   gmx grompp -f md.mdp -c init.gro -p topol.top -o md.tpr
   nohup gmx mdrun -deffnm md -plumed plumed.dat -ntmpi 1 -ntomp 4 -pin on -pinoffset 20 -pinstride 1 -gpu_id 0 -nb gpu -pme gpu -bonded gpu  &
   cd path_to_MD/md1
   gmx grompp -f md.mdp -c init.gro -p topol.top -o md.tpr
   nohup gmx mdrun -deffnm md -plumed plumed.dat -ntmpi 1 -ntomp 4 -pin on -pinoffset 24 -pinstride 1 -gpu_id 1 -nb gpu -pme gpu -bonded gpu &
   cd path_to_MD/md2
   gmx grompp -f md.mdp -c init.gro -p topol.top -o md.tpr
   nohup gmx mdrun -deffnm md -plumed plumed.dat  -ntmpi 1 -ntomp 4 -pin on -pinoffset 28 -pinstride 1 -gpu_id 2 -nb gpu -pme gpu -bonded gpu &
   wait

   for ((i=1;i<=99;i++))
   do
       cd path_to_MD/md0
       mv md* ../temp
       mv ../md2/md* ../md0
       mv ../md1/md* ../md2
       mv ../temp/md* ../md1

       cd path_to_MD/md0
       gmx convert-tpr -s md.tpr -o  md.tpr -extend 100
       nohup gmx mdrun -deffnm md -plumed plumed.dat -cpi md.cpt -append -ntmpi 1 -ntomp 4 -pin on -pinoffset 20 -pinstride 1 -gpu_id 0 -nb gpu -pme gpu -bonded gpu  & 
       rm \#md.* bck*

       cd path_to_MD/md1
       gmx convert-tpr -s md.tpr -o  md.tpr -extend 100
       nohup gmx mdrun -deffnm md -plumed plumed.dat -cpi md.cpt -append -ntmpi 1 -ntomp 4 -pin on -pinoffset 24 -pinstride 1 -gpu_id 1 -nb gpu -pme gpu -bonded gpu  &
       rm \#md.* bck*

       cd path_to_MD/md2
       gmx convert-tpr -s md.tpr -o  md.tpr -extend 100
       nohup gmx mdrun -deffnm md -plumed plumed.dat -cpi md.cpt -append -ntmpi 1 -ntomp 4 -pin on -pinoffset 28 -pinstride 1 -gpu_id 2 -nb gpu -pme gpu -bonded gpu &
       rm \#md.* bck*
      
       wait
   done

   cd path_to_MD/md0
   mv COLVAR COLVAR$j
   mv HILLS HILLS$j
   mv COLVAR$j CV
   mv HILLS$j CV
   touch  COLVAR
   touch  HILLS
   mv md.xtc md${j}.xtc 
   mv md.log md${j}.log 
   mv md.tpr md${j}.tpr
   mv md.trr md${j}.trr
   mv md${j}.xtc md${j}.log md${j}.tpr md${j}.trr MD
   cd path_to_MD/md0/CV
   cat   COLVAR${j} >> COLVAR_ALL

   cd path_to_MD/md1
   mv COLVAR COLVAR$j
   mv HILLS HILLS$j
   mv COLVAR$j CV
   mv HILLS$j CV
   touch  COLVAR
   touch  HILLS
   mv md.xtc md${j}.xtc 
   mv md.log md${j}.log 
   mv md.tpr md${j}.tpr
   mv md.trr md${j}.trr
   mv md${j}.xtc md${j}.log md${j}.tpr md${j}.trr MD
   cd path_to_MD/md1/CV
   cat   COLVAR${j} >> COLVAR_ALL

   cd path_to_MD/md2
   mv COLVAR COLVAR$j
   mv HILLS HILLS$j
   mv COLVAR$j CV
   mv HILLS$j CV
   touch  COLVAR
   touch  HILLS
   mv md.xtc md${j}.xtc 
   mv md.log md${j}.log 
   mv md.tpr md${j}.tpr
   mv md.trr md${j}.trr
   mv md${j}.xtc md${j}.log md${j}.tpr md${j}.trr MD
   cd path_to_MD/md2/CV
   cat   COLVAR${j} >> COLVAR_ALL
   
   cd path_to_MD
   var=`python3 CV_analysis.py` 
   traj=`echo $var |awk '{print $1}'`
   step=`echo $var |awk '{print $2}'`
   frame=`echo $var |awk '{print $3}'`
   mv select.txt select${j}.txt
   mv select${j}.txt SELECT
 
   cd path_to_MD/md${traj}/MD
   echo 0|gmx trjconv -f md${step}.xtc -s md${step}.tpr -dump $frame -o init.gro
   scp init.gro path_to_MD/md0
   scp init.gro path_to_MD/md1
   scp init.gro path_to_MD/md2


done 
