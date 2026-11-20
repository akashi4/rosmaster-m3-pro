# Architecture Logicielle — Yahboom ROSMASTER M3 Pro

## 1. Système d'exploitation & Middleware

- **OS & ROS :** **Ubuntu** + **ROS2 Humble**.
- **Docker :** Sur les variantes **Raspberry Pi 5** et **Jetson Nano (B01)**, l'environnement ROS2 Humble est déployé via **conteneurs Docker** fournis par Yahboom.
- **Pont bas niveau :** **micro-ROS** entre la carte hôte (SBC) et le microcontrôleur **STM32** (publication des topics IMU, odométrie, commande de vitesse `cmd_vel` et contrôle des servos).

## 2. Structure du cursus et des modules logiciels Yahboom

D'après la documentation officielle (`YahboomTechnology/ROSMASTER-M3PRO`), la pile logicielle couvre les modules suivants :

0. **Configuration et mise en route :** Flash système, configuration réseau, déploiement Docker.
1. **Contrôle du châssis :** Bases ROS2, pilotage des moteurs Mecanum, lecture IMU/odométrie, contrôle manette.
2. **LiDAR & SLAM :** Fusion/exploitation des deux LiDARs **T-Mini Plus** pour la cartographie 360° (SLAM) et la détection d'obstacles.
3. **Caméra de profondeur & Vision :** Intégration OpenCV, traitement des flux RGB-D de la **DABAI DCW2**, détection et suivi d'objets.
4. **Bras robotique & Saisie 3D :** Cinématique, simulation et planification sous **MoveIt**, préhension coordonnée dans l'espace 3D.
5. **Navigation autonome :** Planification de réseau routier (*road network planning*), navigation autonome et évitement d'obstacles.
6. **IA & Multimodalité :** Reconnaissance vocale (ASR), traitement du langage naturel (NLP), synthèse vocale, intégration de grands modèles (LLM / VLM) et système **RAG** extensible.
7. **Agents autonomes (OpenClaw) :** Planification de tâches complexes par agent (tri d'objets, inspection, navigation sur commande vocale).
