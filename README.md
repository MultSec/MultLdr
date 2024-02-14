<div align="center">
  <img width="125px" src="assets/MultLdr.png" />
  <h1>MultLdr</h1>
  <br/>

  <p><i>MultLdr is a modular payload loader generator, created by <a href="https://infosec.exchange/@Pengrey">@Pengrey</a>.</i></p>
  <br />
  
</div>

>:warning: **This project is still in development, and is not ready for use.**

## Quick Start

MultLdr requires the usage of Docker, although it is possible to run it without it. If you do not have Docker installed, you can install it [here](https://docs.docker.com/get-docker/).

### Installation

```bash
git clone <repo>
cd MultLdr
docker build -t multldr .
```

### Features

- Payload placement
    - [ ] .data & .rdata
    - [ ] .rsrc
    - [ ] .text
- Payload encryption
    - [ ] AES
    - [ ] RC4
    - [ ] XOR
    - [ ] Bruteforce key
- Payload compression
    - [ ] LZMA
- Payload obfuscation
    - [ ] IPv4/IPv6Fuscation
    - [ ] MACFuscation
    - [ ] UUIDFuscation
- Payload Injection
    - [ ] Thread Hijacking (local)
    - [ ] Thread Hijacking (remote)
    - [ ] Thread Hijacking (apc)
    - [ ] Thread Hijacking (early bird apc)
    - [ ] Callback Injection
    - [ ] Local Mapping Injection (local)
    - [ ] Local Mapping Injection (remote)
    - [ ] Function Stomping (local)
    - [ ] Function Stomping (remote)
    - [ ] Fibers
    - [ ] Threadless Injection
    - [ ] Module Stomping
    - [ ] Module Overloading
    - [ ] Process Hollowing
    - [ ] Ghost Process Injection
    - [ ] Herpaderping Process Injection
    - [ ] Transacted Hollowing
    - [ ] Ghostly Hollowing
    - [ ] Herpaderply Hollowing
- IAT Hiding & Obfuscation
    - [ ] API Hashing
    - [ ] Custom Pseudo Handles
    - [ ] Camouflage
- Unhooking
    - [ ] From Disk
    - [ ] From KnownDLLs
    - [ ] From Suspended Process
    - [ ] From Web Server
    - [ ] Block DLL Policy
    - Direct Syscall
        - [ ] Hell's Gate
    - Indirect Syscall
        - [ ] HellsHall

- [ ] Anti Debugging
- [ ] Anti VM
- [ ] DRM Protection
- [ ] Binary Intropy Reduction
- [ ] PPID Spoofing
- [ ] Arguments Spoofing
- [ ] Binary signing
- [ ] Binary metadata modification
- [ ] Binary bloating
- [ ] CRT Removal