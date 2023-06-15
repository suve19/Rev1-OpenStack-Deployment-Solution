# !/usr/bin/env python

import openstack


def cleanup(openrc_file, tag):
    conn = openstack.connect(cloud=openrc_file)

    # Remove nodes
    nodes = conn.compute.servers(tags=tag)
    for node in nodes:
        node.delete()

    # Remove security groups
    sec_groups = conn.network.security_groups()
    for sec_group in sec_groups:
        if sec_group.name != "default":
            sec_group.delete()

    # Remove router
    router = conn.network.find_router("rev1_router")
    router_interfaces = router.interfaces()
    for interface in router.interfaces:
        router.remove_interface(**interface)

    conn.network.delete_router(router)

    # Remove subnet
    subnet = conn.network.find_subnet("rev1_subnet")
    conn.delete_subnet(subnet)

    # Remove network
    network = conn.network.find_network("rev1_network")
    conn.delete_network(network)

    # Remove keypair
    keypair = conn.compute.find_keypair("rev1_key")
    conn.delete_keypair(keypair)

    # Remove floating IPs
    floating_ips = conn.network.ips(floating_ip=True)
    for floating_ip in floating_ips:
        if "rev1" in floating_ip.name:
            conn.network.delete_ip(floating_ip)

    print("Cleanup complete.")


if __name__ == '__main__':
    openrc_file = "my_openrc_file"
    tag = "MyRev1Tag"
    cleanup(openrc_file, tag)