from ipaddress import ip_address
import os,time
os.environ['SDE'] = "/".join(os.environ['PATH'].split(":")[0].split("/"))
os.environ['SDE_INSTALL'] = "/".join([os.environ['SDE'], 'install'])
print("%env SDE         {}".format(os.environ['SDE']))
print("%env SDE_INSTALL {}".format(os.environ['SDE_INSTALL']))


p4 = bfrt.rate_limit.pipe

p4.Ingress.mi_meter.add(meter_index = 0, meter_spec_cir_kbps = 20, meter_spec_pir_kbps = 30,meter_spec_cbs_kbits = 30, meter_spec_pbs_kbits = 40)
p4.Ingress.mi_meter.add(meter_index = 1, meter_spec_cir_kbps = 20, meter_spec_pir_kbps = 30,meter_spec_cbs_kbits = 30, meter_spec_pbs_kbits = 40)
p4.Ingress.mi_meter.add(meter_index = 2, meter_spec_cir_kbps = 20, meter_spec_pir_kbps = 30,meter_spec_cbs_kbits = 30, meter_spec_pbs_kbits = 40)
p4.Ingress.mi_meter.add(meter_index = 3, meter_spec_cir_kbps = 20, meter_spec_pir_kbps = 30,meter_spec_cbs_kbits = 30, meter_spec_pbs_kbits = 40)

p4.Ingress.meter_rate_limit.add_with_send(meter_color = 0, port = 144)
p4.Ingress.meter_rate_limit.add_with_send(meter_color = 1, port = 144)
p4.Ingress.meter_rate_limit.add_with_drop(meter_color = 2)
# p4.Ingress.ipv4_host.add_with_send(dst_addr=ip_address('11.11.11.200'), port=144)
