with open(r'02_Labs_Assignments\auction-quad-dashboard\build_upgraded_html.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Improve Camera & Studio Lighting in initModalThreeJS
old_init = '''    mCamera = new THREE.PerspectiveCamera(40, width / height, 0.1, 100);
    mCamera.position.set(0, 3.8, 6.2);

    mRenderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
    mRenderer.setSize(width, height);
    mRenderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    mControls = new THREE.OrbitControls(mCamera, mRenderer.domElement);
    mControls.enableDamping = true;
    mControls.dampingFactor = 0.05;
    mControls.enablePan = false;
    mControls.minDistance = 4;
    mControls.maxDistance = 10;
    mControls.maxPolarAngle = Math.PI / 2 - 0.05;

    // Studio Lighting
    const ambient = new THREE.AmbientLight(0xffffff, 0.7);
    mScene.add(ambient);

    const dirLight = new THREE.DirectionalLight(0xffffff, 1.3);
    dirLight.position.set(5, 8, 5);
    mScene.add(dirLight);

    const fillLight = new THREE.PointLight(0x38bdf8, 2, 10);
    fillLight.position.set(-3, 3, 2);
    mScene.add(fillLight);

    const rimLight = new THREE.PointLight(0xf97316, 2, 10);
    rimLight.position.set(3, 2, 2);
    mScene.add(rimLight);'''

new_init = '''    mCamera = new THREE.PerspectiveCamera(40, width / height, 0.1, 100);
    mCamera.position.set(0, 4.4, 5.4); // Higher elevation for better top-down visibility

    mRenderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
    mRenderer.setSize(width, height);
    mRenderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    mRenderer.toneMapping = THREE.ACESFilmicToneMapping;
    mRenderer.toneMappingExposure = 1.05;

    mControls = new THREE.OrbitControls(mCamera, mRenderer.domElement);
    mControls.enableDamping = true;
    mControls.dampingFactor = 0.05;
    mControls.enablePan = false;
    mControls.target.set(0, 0.7, 0);
    mControls.minDistance = 3.5;
    mControls.maxDistance = 9;
    mControls.maxPolarAngle = Math.PI / 2 - 0.05;

    // Studio Lighting (Balanced key, fill, and rim to avoid overexposure)
    const ambient = new THREE.AmbientLight(0xffffff, 0.55);
    mScene.add(ambient);

    const dirLight = new THREE.DirectionalLight(0xffffff, 0.95);
    dirLight.position.set(4, 7, 4);
    mScene.add(dirLight);

    const fillLight = new THREE.PointLight(0x38bdf8, 1.5, 12);
    fillLight.position.set(-3, 3, 2);
    mScene.add(fillLight);

    const rimLight = new THREE.PointLight(0xf97316, 1.4, 12);
    rimLight.position.set(3, 2, -2);
    mScene.add(rimLight);'''

assert old_init in code, "old_init not found in build_upgraded_html.py"
code = code.replace(old_init, new_init, 1)

# 2. Refine Coffee cup colors & Croissant pastry tones
old_coffee_models = '''    } else if (pName === 'ลาเต้' || pName === 'คาปูชิโน' || pName === 'อเมริกาโน') {
      // 1. Ceramic Saucer
      const saucerGeo = new THREE.CylinderGeometry(1.65, 1.35, 0.08, 48);
      const saucerMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.15, metalness: 0.1 });
      const saucer = new THREE.Mesh(saucerGeo, saucerMat);
      saucer.position.y = 0.04;
      m.add(saucer);

      const lipGeo = new THREE.TorusGeometry(1.55, 0.04, 16, 48);
      const lip = new THREE.Mesh(lipGeo, saucerMat);
      lip.rotation.x = Math.PI / 2;
      lip.position.y = 0.08;
      m.add(lip);

      // 2. Ceramic Coffee Cup Body
      const cupGeo = new THREE.CylinderGeometry(1.05, 0.75, 1.15, 48);
      const cupMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.15, metalness: 0.1 });
      const cup = new THREE.Mesh(cupGeo, cupMat);
      cup.position.y = 0.65;
      m.add(cup);

      // Cup Rim
      const rimGeo = new THREE.TorusGeometry(1.05, 0.05, 16, 48);
      const rim = new THREE.Mesh(rimGeo, cupMat);
      rim.rotation.x = Math.PI / 2;
      rim.position.y = 1.22;
      m.add(rim);

      // 3. Ergonomic Handle
      const handleGeo = new THREE.TorusGeometry(0.38, 0.08, 16, 32, Math.PI * 1.3);
      const handle = new THREE.Mesh(handleGeo, cupMat);
      handle.rotation.z = -Math.PI / 6;
      handle.position.set(1.15, 0.65, 0);
      m.add(handle);'''

new_coffee_models = '''    } else if (pName === 'ลาเต้' || pName === 'คาปูชิโน' || pName === 'อเมริกาโน') {
      // 1. Ceramic Saucer (Elegant Matte Navy / Slate Ceramic)
      const saucerGeo = new THREE.CylinderGeometry(1.65, 1.35, 0.08, 48);
      const ceramicMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.35, metalness: 0.2 });
      const saucer = new THREE.Mesh(saucerGeo, ceramicMat);
      saucer.position.y = 0.04;
      m.add(saucer);

      const lipGeo = new THREE.TorusGeometry(1.55, 0.04, 16, 48);
      const lip = new THREE.Mesh(lipGeo, ceramicMat);
      lip.rotation.x = Math.PI / 2;
      lip.position.y = 0.08;
      m.add(lip);

      // 2. Ceramic Coffee Cup Body
      const cupGeo = new THREE.CylinderGeometry(1.05, 0.75, 1.15, 48);
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
      m.add(handle);'''

assert old_coffee_models in code, "old_coffee_models not found in build_upgraded_html.py"
code = code.replace(old_coffee_models, new_coffee_models, 1)

# 3. Refine Croissant color to baked golden-brown
old_croissant = '''        const crustColor = (i % 2 === 0) ? 0xcc7722 : 0xd9822b;
        const segMat = new THREE.MeshStandardMaterial({ color: crustColor, roughness: 0.6 });'''

new_croissant = '''        const crustColor = (i % 2 === 0) ? 0x9a521a : 0xbf6c26; // Golden-brown baked crust
        const segMat = new THREE.MeshStandardMaterial({ color: crustColor, roughness: 0.7, metalness: 0.05 });'''

assert old_croissant in code, "old_croissant not found in build_upgraded_html.py"
code = code.replace(old_croissant, new_croissant, 1)

with open(r'02_Labs_Assignments\auction-quad-dashboard\build_upgraded_html.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("SUCCESS: Refined 3D camera angle, lighting, and materials in build_upgraded_html.py")
