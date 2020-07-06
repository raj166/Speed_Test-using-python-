from speedtest import Speedtest
st = Speedtest()

print("Download :" , int(st.download())//(1024*1024), end= "")
print(" Mbps")
print("upload :", int(st.upload())//(1024*1024), end= "")
print(" Mbps")
st.get_servers([])
print("ping :", st.results.ping)