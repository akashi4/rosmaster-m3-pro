# Spécifications Matérielles — Yahboom ROSMASTER M3 Pro

## 1. Variantes de carte contrôleur principale (Host / SBC)

Le ROSMASTER M3 Pro est décliné en plusieurs éditions selon la carte de calcul embarquée :

| Variante | Mémoire (RAM) | Cas d'usage typique | Environnement ROS2 |
| :--- | :--- | :--- | :--- |
| **NVIDIA Jetson Orin NX Super** | 8 Go / 16 Go | Inférence IA lourde en local (LLM, VLM, réseaux profonds complexes) | Natif Ubuntu + ROS2 Humble |
| **NVIDIA Jetson Orin Nano Super** | 4 Go / 8 Go | Navigation ROS2, vision par ordinateur et deep learning accéléré GPU | Natif Ubuntu + ROS2 Humble |
| **NVIDIA Jetson Nano (B01)** | 4 Go (SUB) | Éducation ROS2 standard et vision par ordinateur basique | Docker ROS2 Humble |
| **Raspberry Pi 5** | 4 Go / 8 Go / 16 Go | Workflows ROS2 standards, nœuds Python légers, apprentissage algorithmique | Docker ROS2 Humble |

---

## 2. Contrôleur bas niveau (MCU) & Capteurs inertiels

- **Carte de contrôle :** Carte contrôleur basée sur **STM32** avec pont **micro-ROS** vers la carte hôte.
- **Fonctions :** Commande des moteurs DC à encodeurs, lecture des encodeurs, pilotage des servomoteurs bus série du bras 6-DOF, gestion de l'alimentation.
- **IMU intégré :** Centrale inertielle **9 axes** (accéléromètre, gyroscope, magnétomètre) intégrée sur la carte STM32 pour l'odométrie, l'estimation d'état et la localisation ROS2.

---

## 3. Châssis & Mobilité

- **Matériau du châssis :** Alliage d'aluminium.
- **Dimensions (corps du châssis) :** env. **19,8 cm × 17,8 cm × 16,8 cm** *(la hauteur totale varie selon la posture du bras robotique et le montage caméra/écran)*.
- **Poids estimé :** env. **3,5 kg à 4,5 kg** assemblé avec bras, batterie et selon la carte hôte / écran optionnel.
- **Roues :** 4 roues omnidirectionnelles **Mecanum de 80 mm** (déplacement avant/arrière, latéral, diagonal et rotation sur place).
- **Suspension :** Suspension arrière indépendante de type **pendulaire** (*pendulum-style suspension*) pour l'absorption des chocs et le franchissement de petites irrégularités.
- **Motorisation :** Moteurs DC avec encodeurs (architecture d'alimentation nominale **12 V / 12,6 V**).

---

## 4. Capteurs de navigation et de vision 3D

### Double LiDAR ToF (Cartographie & Évitement d'obstacles)
- **Modèle :** **2 × YDLIDAR T-Mini Plus** (LiDAR laser Time-of-Flight).
- **Implantation :** Disposition diagonale décalée (**avant-gauche** et **arrière-droite**) pour une couverture complète à **360°** tout en réduisant les angles morts liés au bras robotique.
- **Portée :** **0,05 m à 12 m**.
- **Fréquence d'échantillonnage :** Jusqu'à **4 000 mesures/s**.

### Caméra de profondeur 3D
- **Modèle :** **Orbbec DABAI DCW2** (caméra stéréo binoculaire à lumière structurée).
- **Portée de profondeur :** Jusqu'à **5 m**.
- **Usages :** Nuages de points 3D, reconnaissance d'objets, suivi visuel, navigation visuelle et préhension 3D avec le bras.

---

## 5. Bras robotique 6-DOF

- **Architecture :** Bras articulé à **6 degrés de liberté (6-DOF)**.
- **Actionneurs :** Servomoteurs intelligents sur **bus série** avec retour de position et d'état.
- **Capacité de préhension (payload) :** Jusqu'à env. **410 g**.
- **Répétabilité :** env. **0,5 mm**.
- **Intégration ROS2 :** Compatible **MoveIt** (cinématique directe/inverse, planification de trajectoire et saisie 3D).

---

## 6. Alimentation & Périphériques optionnels

- **Batterie :** Pack batterie haute capacité **9 600 mAh** (12,6 V).
- **Chargeur :** Chargeur DC **12,6 V / 2 A**.
- **Écran (optionnel) :** Écran tactile **IPS HD 7 pouces** pour l'affichage local et le retour d'interface.
- **Audio :** Haut-parleurs intégrés et module de capture/reconnaissance vocale pour les interactions IA multimodales.
