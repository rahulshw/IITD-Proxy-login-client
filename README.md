# PROXY LOGIN CLIENT FOR IITD

## How to use?
1. Run the commands below after cloning this repo
   ```shell
   cd iitd_proxy_login
   python login.py
   ```

2. Add proxy for command line applications by running the commands below
   ```shell
   proxynum = 21 # (for IRD staffs, for others check the section:Proxy number)
   export http_proxy=http://proxy${proxynum}.iitd.ernet.in:3128
   export https_proxy=https://proxy${proxynum}.iitd.ernet.in:3128
   export HTTP_PROXY=$http_proxy
   export HTTPS_PROXY=$https_proxy
   ```
4. Check if the internet is working by running 
   ```
   curl -I https://www.google.com
   # this should return HTTP/2 200
   ```


## Proxy number
```yaml
btech: 22
dual: 62
diit: 21
faculty: 82
integrated: 21
mtech: 62
phd: 61
retfaculty: 82
staff: 21
irdstaff: 21
mba: 21
mdes: 21
msc: 21
msr: 21
pgdip: 21
```