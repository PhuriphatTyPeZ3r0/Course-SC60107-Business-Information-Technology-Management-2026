with open(r'02_Labs_Assignments\auction-quad-dashboard\build_upgraded_html.py', 'r', encoding='utf-8') as f:
    code = f.read()

target = '''      // 2. Ceramic Coffee Cup Body
      const cupGeo = new THREE.CylinderGeometry(1.05, 0.75, 1.15, 48);
      const ceramicMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.35, metalness: 0.2 });
      const cup = new THREE.Mesh(cupGeo, ceramicMat);
      cup.position.y = 0.65;
      m.add(cup);

      // Gold / Ceramic Rim
      const rimGeo = new THREE.TorusGeometry(1.05, 0.045, 16, 48);
      const rimMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, roughness: 0.3, metalness: 0.7 });
      const rim = new THREE.Mesh(rimGeo, rimMat);
      rim.rotation.x = Math.PI / 2;
      rim.position.y = 1.22;
      m.add(rim);

      // 3. Ergonomic Handle
      const handleGeo = new THREE.TorusGeometry(0.38, 0.08, 16, 32, Math.PI * 1.3);
      const handle = new THREE.Mesh(handleGeo, ceramicMat);
      handle.rotation.z = -Math.PI / 6;
      handle.position.set(1.15, 0.65, 0);
      m.add(handle);

      // 4. Coffee Liquid
      const isAmericano = (pName === 'อเมริกาโน');
      const isCappuccino = (pName === 'คาปูชิโน');
      const coffeeColor = isAmericano ? 0x221206 : (isCappuccino ? 0x613b1e : 0x784a27);
      const coffeeGeo = new THREE.CylinderGeometry(0.98, 0.98, 0.05, 36);
      const coffeeMat = new THREE.MeshStandardMaterial({ color: coffeeColor, roughness: 0.15 });
      const coffee = new THREE.Mesh(coffeeGeo, coffeeMat);
      coffee.position.y = 1.15;
      m.add(coffee);

      if (pName === 'ลาเต้') {
        // Latte Art Foam + Heart
        const foamGeo = new THREE.RingGeometry(0.1, 0.65, 32);
        const foamMat = new THREE.MeshStandardMaterial({ color: 0xfffae8, roughness: 0.4, side: THREE.DoubleSide });
        const foam = new THREE.Mesh(foamGeo, foamMat);
        foam.rotation.x = -Math.PI / 2;
        foam.position.y = 1.18;
        m.add(foam);

        const heartGeo = new THREE.CircleGeometry(0.28, 32);
        const heart = new THREE.Mesh(heartGeo, foamMat);
        heart.rotation.x = -Math.PI / 2;
        heart.position.y = 1.181;
        m.add(heart);
      } else if (isCappuccino) {
        // Thick foamy milk dome
        const capFoamGeo = new THREE.CylinderGeometry(0.96, 0.96, 0.1, 36);
        const capFoamMat = new THREE.MeshStandardMaterial({ color: 0xfffcf5, roughness: 0.5 });
        const capFoam = new THREE.Mesh(capFoamGeo, capFoamMat);
        capFoam.position.y = 1.18;
        m.add(capFoam);

        // Cocoa dust sprinkles on foam
        for (let i = 0; i < 18; i++) {
          const dustGeo = new THREE.BoxGeometry(0.04, 0.01, 0.04);
          const dustMat = new THREE.MeshStandardMaterial({ color: 0x451a03, roughness: 0.9 });
          const dust = new THREE.Mesh(dustGeo, dustMat);
          const r = Math.random() * 0.65;
          const theta = Math.random() * Math.PI * 2;
          dust.position.set(Math.cos(theta) * r, 1.235, Math.sin(theta) * r);
          m.add(dust);
        }
      }'''

replacement = '''      // 2. Ceramic Coffee Cup Body (Hollow with double-sided ceramic)
      const cupGeo = new THREE.CylinderGeometry(1.05, 0.75, 1.15, 48, 1, true);
      const ceramicMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.35, metalness: 0.2, side: THREE.DoubleSide });
      const cup = new THREE.Mesh(cupGeo, ceramicMat);
      cup.position.y = 0.65;
      m.add(cup);

      // Gold Ceramic Rim
      const rimGeo = new THREE.TorusGeometry(1.05, 0.045, 16, 48);
      const rimMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, roughness: 0.3, metalness: 0.7 });
      const rim = new THREE.Mesh(rimGeo, rimMat);
      rim.rotation.x = Math.PI / 2;
      rim.position.y = 1.22;
      m.add(rim);

      // 3. Ergonomic Handle
      const handleGeo = new THREE.TorusGeometry(0.38, 0.08, 16, 32, Math.PI * 1.3);
      const handle = new THREE.Mesh(handleGeo, ceramicMat);
      handle.rotation.z = -Math.PI / 6;
      handle.position.set(1.15, 0.65, 0);
      m.add(handle);

      // 4. Coffee Liquid Surface (Planar circular disk visible from above)
      const isAmericano = (pName === 'อเมริกาโน');
      const isCappuccino = (pName === 'คาปูชิโน');
      const coffeeColor = isAmericano ? 0x221206 : (isCappuccino ? 0x543217 : 0x784a27);
      const coffeeGeo = new THREE.CircleGeometry(1.02, 48);
      const coffeeMat = new THREE.MeshStandardMaterial({ color: coffeeColor, roughness: 0.2 });
      const coffee = new THREE.Mesh(coffeeGeo, coffeeMat);
      coffee.rotation.x = -Math.PI / 2;
      coffee.position.y = 1.18;
      m.add(coffee);

      if (pName === 'ลาเต้') {
        // Latte Art Foam + Heart Emblem
        const foamGeo = new THREE.RingGeometry(0.12, 0.72, 32);
        const foamMat = new THREE.MeshStandardMaterial({ color: 0xfffae8, roughness: 0.4, side: THREE.DoubleSide });
        const foam = new THREE.Mesh(foamGeo, foamMat);
        foam.rotation.x = -Math.PI / 2;
        foam.position.y = 1.185;
        m.add(foam);

        const heartGeo = new THREE.CircleGeometry(0.32, 32);
        const heart = new THREE.Mesh(heartGeo, foamMat);
        heart.rotation.x = -Math.PI / 2;
        heart.position.y = 1.188;
        m.add(heart);
      } else if (isCappuccino) {
        // Thick foamy milk dome
        const capFoamGeo = new THREE.CircleGeometry(0.96, 48);
        const capFoamMat = new THREE.MeshStandardMaterial({ color: 0xfffcf5, roughness: 0.5 });
        const capFoam = new THREE.Mesh(capFoamGeo, capFoamMat);
        capFoam.rotation.x = -Math.PI / 2;
        capFoam.position.y = 1.185;
        m.add(capFoam);

        // Cocoa dust sprinkles on foam
        for (let i = 0; i < 20; i++) {
          const dustGeo = new THREE.BoxGeometry(0.04, 0.01, 0.04);
          const dustMat = new THREE.MeshStandardMaterial({ color: 0x451a03, roughness: 0.9 });
          const dust = new THREE.Mesh(dustGeo, dustMat);
          const r = Math.random() * 0.65;
          const theta = Math.random() * Math.PI * 2;
          dust.position.set(Math.cos(theta) * r, 1.19, Math.sin(theta) * r);
          m.add(dust);
        }
      }'''

assert target in code, "Target not found in build_upgraded_html.py"
code = code.replace(target, replacement, 1)

with open(r'02_Labs_Assignments\auction-quad-dashboard\build_upgraded_html.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("SUCCESS: Updated coffee cup geometry and liquid visibility")
