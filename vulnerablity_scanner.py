#!/usr/bin/env pyhton

import scanner


target_url = "http://192.168.**.**/dvwa/"
links_to_ignore = ["http://192.168.**.**/dvwa/logout.php"]

data_dict = {"username": "admin", "password": "password", "Login": "submit"}

vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
vuln_scanner.session.post("http://192.168.**.**/dvwa/login.php", data=data_dict)

vuln_scanner.crawl()
vuln_scanner.run_scanner()