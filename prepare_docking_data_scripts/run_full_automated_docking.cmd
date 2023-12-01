bash -c "sed -i.bak 's/\r$//' automated_docking.sh"
bash -c "sed -i.bak 's/\r$//' install_autodock.sh"
bash -c "sed -i.bak 's/\r$//' run_vina_split.sh"
bash automated_docking.sh
pause()