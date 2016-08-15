for i in spfRawData/rawSPF/*.csv; do
    python3 helpers.py $(basename $i) spfRawData/rawSPF/ procSPF/
done
