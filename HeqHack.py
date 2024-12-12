import pymem
import pymem.process

memory = pymem.Pymem("cs2.exe")
player = pymem.process.module_from_name(memory.process_handle, "client.dll")

dwLocalPlayerPawn = memory.read_longlong(player.lpBaseOfDll + 0x1855CE8)
dwViewRender = memory.read_longlong(player.lpBaseOfDll + 0x1A54D60)
dwLocalPlayerController = memory.read_longlong(player.lpBaseOfDll + 0x1A41FD0)
dwEntityList = memory.read_longlong(player.lpBaseOfDll + 0x19F2488)
dwGlowManager = memory.read_longlong(player.lpBaseOfDll + 0x1A4F5A8)

memory.write_int(dwLocalPlayerController + 0x6F4, 90)
memory.write_float(dwLocalPlayerPawn + 0x1408, 1.0)
memory.write_float(dwLocalPlayerPawn + 0x14B0, 1.0)
memory.write_float(dwLocalPlayerPawn + 0x14B4, 1.0)