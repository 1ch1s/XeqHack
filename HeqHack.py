import pymem
import pymem.process

sperma = pymem.Pymem("cs2.exe")
igrok = pymem.process.module_from_name(sperma.process_handle, "client.dll")

dwLocalPlayerPawn = sperma.read_longlong(igrok.lpBaseOfDll + 0x1855CE8)
dwViewRender = sperma.read_longlong(igrok.lpBaseOfDll + 0x1A54D60)
dwLocalPlayerController = sperma.read_longlong(igrok.lpBaseOfDll + 0x1A41FD0)
dwEntityList = sperma.read_longlong(igrok.lpBaseOfDll + 0x19F2488)
dwGlowManager = sperma.read_longlong(igrok.lpBaseOfDll + 0x1A4F5A8)

sperma.write_int(dwLocalPlayerController + 0x6F4, 90)
sperma.write_float(dwLocalPlayerPawn + 0x1408, 1.0)
sperma.write_float(dwLocalPlayerPawn + 0x14B0, 1.0)
sperma.write_float(dwLocalPlayerPawn + 0x14B4, 1.0)