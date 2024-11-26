def test_cif_exploit():    
    from pymatgen.io.cif import CifParser
    parser = CifParser("/home/kali/Workspace_Ethical_Hacking/hack_the_box/htb_machines/chemistry/vuln.cif")
    structure = parser.parse_structures()