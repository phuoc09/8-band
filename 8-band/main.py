import process
# chia làm 8 bộ loc 50, 100, 200, 400, 800, 1600, 2400, 3200 Hz

process.fir_bpf('pi.wav','./tach/50.wav',50,100,500)
process.fir_bpf('pi.wav','./tach/100.wav',100,200,500)
process.fir_bpf('pi.wav','./tach/200.wav',200,400,500)
process.fir_bpf('pi.wav','./tach/400.wav',400,800,500)
process.fir_bpf('pi.wav','./tach/800.wav',800,1600,500)
process.fir_bpf('pi.wav','./tach/1600.wav',1600,2400,500)
process.fir_bpf('pi.wav','./tach/2400.wav',2400,3200,500)
process.fir_hpf('pi.wav','./tach/3200.wav',3200,500)

process.amplify_wav('./tach/50.wav','./equalizer/50.wav',5)
process.amplify_wav('./tach/100.wav','./equalizer/100.wav',5)
process.amplify_wav('./tach/200.wav','./equalizer/200.wav',1)
process.amplify_wav('./tach/400.wav','./equalizer/400.wav',0)
process.amplify_wav('./tach/800.wav','./equalizer/800.wav',-1)
process.amplify_wav('./tach/1600.wav','./equalizer/1600.wav',3)
process.amplify_wav('./tach/2400.wav','./equalizer/2400.wav',1)
process.amplify_wav('./tach/3200.wav','./equalizer/3200.wav',1)

process.add_amplitude('./equalizer','output.wav')