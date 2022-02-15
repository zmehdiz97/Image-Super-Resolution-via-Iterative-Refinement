if [ $1 == "srun_tp" ]
then srun -N 1 --exclusive -p gpu_tp -t 2:00:00 --pty bash
fi

if [ $1 == "sbatch" ]
then sbatch -N 1 --exclusive -p gpu_prod_night batch.sh
fi
#sbatch -N 1 --exclusive -p gpu_prod_long batch.sh