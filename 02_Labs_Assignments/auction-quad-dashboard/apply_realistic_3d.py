import re

# Read current build_upgraded_html.py
with open(r'02_Labs_Assignments\auction-quad-dashboard\build_upgraded_html.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update <head> to add GLTFLoader
old_head_scripts = '''<!-- Three.js & OrbitControls for 3D Pop-up -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>'''

new_head_scripts = '''<!-- Three.js, OrbitControls & GLTFLoader for 3D Pop-up -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>'''

assert old_head_scripts in content, "old_head_scripts not found!"
content = content.replace(old_head_scripts, new_head_scripts, 1)
print("Step 1: Added GLTFLoader script tag")

# 2. Update CSS for 3D Box & Toolbar
old_css = '''.modal-3d-box {{
  position: relative;
  background: radial-gradient(circle at center, rgba(37,99,235,.08) 0%, transparent 70%);
  display: flex;
  align-items: center;
  justify-content: center;
  border-right: 1px solid var(--glass-b);
  min-height: 280px;
  cursor: grab;
}}
.modal-3d-box:active {{ cursor: grabbing; }}'''

new_css = '''.modal-3d-box {{
  position: relative;
  background: radial-gradient(circle at center, rgba(37,99,235,.08) 0%, transparent 70%);
  display: flex;
  align-items: center;
  justify-content: center;
  border-right: 1px solid var(--glass-b);
  min-height: 320px;
  cursor: grab;
  transition: border-color 0.2s, background 0.2s;
}}
.modal-3d-box:active {{ cursor: grabbing; }}
.modal-3d-box.dragover {{
  border: 2px dashed var(--cyan) !important;
  background: radial-gradient(circle at center, rgba(56,189,248,.18) 0%, transparent 70%) !important;
}}

.modal-3d-toolbar {{
  position: absolute;
  top: 10px;
  left: 10px;
  right: 10px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  z-index: 10;
  pointer-events: none;
}}
.modal-3d-toolbar > * {{
  pointer-events: auto;
}}

.btn-glb {{
  display: inline-flex;
  align-items: center;
  gap: 4px;
  background: var(--nav-bg);
  border: 1px solid var(--glass-b);
  color: var(--txt);
  font-family: var(--font);
  font-size: 11px;
  font-weight: 500;
  padding: 4px 10px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}}
.btn-glb:hover {{
  background: var(--blue);
  color: #fff;
  border-color: var(--blue-l);
}}
.btn-glb .i {{ font-size: 14px; }}'''

assert old_css in content, "old_css not found!"
content = content.replace(old_css, new_css, 1)
print("Step 2: Added CSS for 3D toolbar & dragover")

# 3. Update HTML for modal-3d-box & stats
old_modal_html = '''      <!-- 3D Stage Box -->
      <div class="modal-3d-box" id="modal3DBox">
        <canvas id="modal3DCanvas"></canvas>
        <div class="modal-3d-hint"><span class="i" style="font-size:14px;">3d_rotation</span> หมุน 360° ด้วยเมาส์</div>
      </div>'''

new_modal_html = '''      <!-- 3D Stage Box -->
      <div class="modal-3d-box" id="modal3DBox">
        <div class="modal-3d-toolbar">
          <span id="modelModeBadge" class="badge" style="font-size:10px;padding:3px 8px;background:rgba(37,99,235,.2);color:var(--cyan);border:1px solid rgba(56,189,248,.3);">
            <span class="i" style="font-size:12px;">auto_awesome</span> โมเดล 3D สมจริง (Studio)
          </span>
          <div style="display:flex;gap:6px;">
            <button id="btnResetModel" class="btn-glb" style="display:none;" onclick="resetToProceduralModel()" title="คืนค่าโมเดลสมจริงตั้งต้น">
              <span class="i">restart_alt</span> รีเซ็ต
            </button>
            <button id="btnImportGLB" class="btn-glb" onclick="document.getElementById('glbFileInput').click()" title="นำเข้าไฟล์ .glb หรือ .gltf Open-Source">
              <span class="i">upload_file</span> นำเข้า .GLB
            </button>
            <input type="file" id="glbFileInput" accept=".glb,.gltf" style="display:none;" onchange="handleGLBFileSelect(event)">
          </div>
        </div>

        <canvas id="modal3DCanvas"></canvas>
        <div class="modal-3d-hint"><span class="i" style="font-size:14px;">3d_rotation</span> หมุน 360° · ซูม · วางไฟล์ .glb ได้</div>
      </div>'''

assert old_modal_html in content, "old_modal_html not found!"
content = content.replace(old_modal_html, new_modal_html, 1)
print("Step 3: Added HTML for 3D toolbar & import button")

# Also add the Open-Source Resource Bar right after branch breakdown in modal
old_branch_end = '''            <div class="m-b-val" id="mValMall">฿3,410</div>
          </div>
        </div>
      </div>'''

new_branch_end = '''            <div class="m-b-val" id="mValMall">฿3,410</div>
          </div>
        </div>

        <!-- Open-Source Resource Bar -->
        <div style="font-size:10px;color:var(--muted);background:var(--card-sub-bg);padding:8px 10px;border-radius:8px;border:1px solid var(--border-sub);display:flex;align-items:center;justify-content:space-between;gap:8px;">
          <div style="display:flex;align-items:center;gap:4px;">
            <span class="i" style="font-size:13px;color:var(--cyan);">hub</span>
            <span>แหล่งโมเดลฟรี: <a href="https://poly.pizza" target="_blank" rel="noopener" style="color:var(--blue-l);text-decoration:none;">Poly.pizza (CC0)</a> · <a href="https://sketchfab.com" target="_blank" rel="noopener" style="color:var(--blue-l);text-decoration:none;">Sketchfab</a></span>
          </div>
          <span style="color:var(--dim);">100% Offline</span>
        </div>
      </div>'''

assert old_branch_end in content, "old_branch_end not found!"
content = content.replace(old_branch_end, new_branch_end, 1)
print("Step 4: Added Open-Source Resource Bar")

# 4. Update JavaScript for 3D engine, custom GLTF loader, and realistic models
old_js_block = '''  // 3D Engine & Modal References (Declared at top of script scope)
  let mScene = null, mCamera = null, mRenderer = null, mControls = null, mMeshGroup = null, mAnimId = null;
  const modalOverlay = document.getElementById('modal3D');'''

new_js_block = '''  // 3D Engine & Modal References (Declared at top of script scope)
  let mScene = null, mCamera = null, mRenderer = null, mControls = null, mMeshGroup = null, mAnimId = null;
  let currentProductItem = null;
  let customGLBModel = null;
  const modalOverlay = document.getElementById('modal3D');'''

assert old_js_block in content, "old_js_block not found!"
content = content.replace(old_js_block, new_js_block, 1)
print("Step 5: Declared currentProductItem and customGLBModel in JS scope")

# Now replace the updateModalMesh and related functions
old_three_engine = '''  function initModalThreeJS() {
    const box = document.getElementById('modal3DBox');
    const canvas = document.getElementById('modal3DCanvas');
    const width = box.clientWidth || 320;
    const height = box.clientHeight || 320;

    mScene = new THREE.Scene();
    const isLight = document.documentElement.getAttribute('data-theme') === 'light';
    mScene.background = new THREE.Color(isLight ? 0xf8fafc : 0x0c162e);

    mCamera = new THREE.PerspectiveCamera(40, width / height, 0.1, 100);
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

    // Lights
    const ambient = new THREE.AmbientLight(0xffffff, 0.7);
    mScene.add(ambient);

    const dirLight = new THREE.DirectionalLight(0xffffff, 1.2);
    dirLight.position.set(5, 8, 5);
    mScene.add(dirLight);

    const pointLight = new THREE.PointLight(0x38bdf8, 2, 10);
    pointLight.position.set(-3, 3, 2);
    mScene.add(pointLight);

    const warmLight = new THREE.PointLight(0xf97316, 2, 10);
    warmLight.position.set(3, 2, 2);
    mScene.add(warmLight);

    // Mesh Group
    mMeshGroup = new THREE.Group();
    mScene.add(mMeshGroup);

    // Base Reflective Disc
    const baseGeo = new THREE.CylinderGeometry(2.2, 2.3, 0.15, 48);
    const baseMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.3, metalness: 0.8 });
    const baseMesh = new THREE.Mesh(baseGeo, baseMat);
    baseMesh.position.y = -0.075;
    mMeshGroup.add(baseMesh);

    // Glowing Neon Ring
    const ringGeo = new THREE.TorusGeometry(2.25, 0.03, 16, 48);
    const ringMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
    const ringMesh = new THREE.Mesh(ringGeo, ringMat);
    ringMesh.rotation.x = Math.PI / 2;
    ringMesh.position.y = 0.02;
    mMeshGroup.add(ringMesh);

    animateModal();
  }

  function updateModalMesh(item) {
    if (!mMeshGroup) return;

    // Remove old item mesh (keep base disc & ring: index 0 and 1)
    while (mMeshGroup.children.length > 2) {
      mMeshGroup.remove(mMeshGroup.children[2]);
    }

    const hexColor = parseInt(item.color.replace('#', '0x'), 16);

    // Create 3D geometry representing product
    const itemGroup = new THREE.Group();

    if (item.category === 'เบเกอรี') {
      // Cake / Pastry tiered cylinder
      const c1Geo = new THREE.CylinderGeometry(1.2, 1.25, 0.8, 36);
      const c1Mat = new THREE.MeshStandardMaterial({ color: hexColor, roughness: 0.25, metalness: 0.5 });
      const c1 = new THREE.Mesh(c1Geo, c1Mat);
      c1.position.y = 0.4;
      itemGroup.add(c1);

      const c2Geo = new THREE.CylinderGeometry(0.8, 0.85, 0.5, 32);
      const c2Mat = new THREE.MeshStandardMaterial({ color: 0xfbbf24, roughness: 0.3, metalness: 0.6 });
      const c2 = new THREE.Mesh(c2Geo, c2Mat);
      c2.position.y = 1.05;
      itemGroup.add(c2);
    } else if (item.category === 'กาแฟ') {
      // Coffee Cup Cylinder with rim
      const cupGeo = new THREE.CylinderGeometry(1.1, 0.85, 1.4, 32);
      const cupMat = new THREE.MeshStandardMaterial({ color: hexColor, roughness: 0.2, metalness: 0.7 });
      const cup = new THREE.Mesh(cupGeo, cupMat);
      cup.position.y = 0.7;
      itemGroup.add(cup);

      // Foam / Lid
      const foamGeo = new THREE.CylinderGeometry(1.05, 1.05, 0.15, 32);
      const foamMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.8 });
      const foam = new THREE.Mesh(foamGeo, foamMat);
      foam.position.y = 1.4;
      itemGroup.add(foam);
    } else {
      // Beverage Prism / Glass
      const bevGeo = new THREE.CylinderGeometry(0.9, 0.7, 1.5, 8);
      const bevMat = new THREE.MeshStandardMaterial({ color: hexColor, roughness: 0.1, metalness: 0.8, transparent: true, opacity: 0.9 });
      const bev = new THREE.Mesh(bevGeo, bevMat);
      bev.position.y = 0.75;
      itemGroup.add(bev);
    }

    mMeshGroup.add(itemGroup);
  }'''

new_three_engine = '''  function clearCurrentModel() {
    if (!mMeshGroup) return;
    while (mMeshGroup.children.length > 2) {
      mMeshGroup.remove(mMeshGroup.children[2]);
    }
  }

  function resetToProceduralModel() {
    customGLBModel = null;
    const btnReset = document.getElementById('btnResetModel');
    if (btnReset) btnReset.style.display = 'none';
    const badge = document.getElementById('modelModeBadge');
    if (badge) {
      badge.innerHTML = '<span class="i" style="font-size:12px;">auto_awesome</span> โมเดล 3D สมจริง (Studio)';
      badge.style.borderColor = 'rgba(56,189,248,.3)';
      badge.style.color = 'var(--cyan)';
    }
    if (currentProductItem) {
      updateModalMesh(currentProductItem);
    }
  }

  function handleGLBFileSelect(e) {
    const file = e.target.files && e.target.files[0];
    if (file) loadGLBFile(file);
    e.target.value = '';
  }

  function loadGLBFile(file) {
    if (!window.THREE || !THREE.GLTFLoader) {
      alert('GLTFLoader ยังโหลดไม่เสร็จหรือออฟไลน์ กรุณาตรวจสอบการเชื่อมต่ออินเทอร์เน็ตสำหรับการโหลดไลบรารี');
      return;
    }
    const reader = new FileReader();
    reader.onload = function(evt) {
      const arrayBuffer = evt.target.result;
      const loader = new THREE.GLTFLoader();
      loader.parse(arrayBuffer, '', (gltf) => {
        clearCurrentModel();
        customGLBModel = gltf.scene;

        // Auto-fit & center the GLTF model
        const bBox = new THREE.Box3().setFromObject(customGLBModel);
        const size = bBox.getSize(new THREE.Vector3());
        const center = bBox.getCenter(new THREE.Vector3());
        const maxDim = Math.max(size.x, size.y, size.z);
        const scale = 2.0 / (maxDim || 1);
        customGLBModel.scale.setScalar(scale);

        // Center on top of base pedestal
        customGLBModel.position.x = -center.x * scale;
        customGLBModel.position.y = -bBox.min.y * scale + 0.05;
        customGLBModel.position.z = -center.z * scale;

        mMeshGroup.add(customGLBModel);

        // Update UI
        const btnReset = document.getElementById('btnResetModel');
        if (btnReset) btnReset.style.display = 'inline-flex';
        const badge = document.getElementById('modelModeBadge');
        if (badge) {
          const shortName = file.name.length > 18 ? file.name.substring(0, 15) + '...' : file.name;
          badge.innerHTML = '<span class="i" style="font-size:12px;">check_circle</span> โมเดล: ' + shortName;
          badge.style.borderColor = 'rgba(16,185,129,.4)';
          badge.style.color = 'var(--green)';
        }
      }, (err) => {
        console.error('Error parsing GLB:', err);
        alert('เกิดข้อผิดพลาดในการเปิดไฟล์ 3D: กรุณาตรวจสอบว่าเป็นไฟล์ .glb หรือ .gltf ที่ถูกต้อง');
      });
    };
    reader.readAsArrayBuffer(file);
  }

  function setupDragAndDrop() {
    const box = document.getElementById('modal3DBox');
    if (!box) return;
    box.addEventListener('dragover', (e) => {
      e.preventDefault();
      box.classList.add('dragover');
    });
    box.addEventListener('dragleave', () => {
      box.classList.remove('dragover');
    });
    box.addEventListener('drop', (e) => {
      e.preventDefault();
      box.classList.remove('dragover');
      if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
        loadGLBFile(e.dataTransfer.files[0]);
      }
    });
  }

  function initModalThreeJS() {
    const box = document.getElementById('modal3DBox');
    const canvas = document.getElementById('modal3DCanvas');
    const width = box.clientWidth || 320;
    const height = box.clientHeight || 320;

    mScene = new THREE.Scene();
    const isLight = document.documentElement.getAttribute('data-theme') === 'light';
    mScene.background = new THREE.Color(isLight ? 0xf8fafc : 0x0c162e);

    mCamera = new THREE.PerspectiveCamera(40, width / height, 0.1, 100);
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
    mScene.add(rimLight);

    // Mesh Group
    mMeshGroup = new THREE.Group();
    mScene.add(mMeshGroup);

    // Base Reflective Disc Pedestal
    const baseGeo = new THREE.CylinderGeometry(2.2, 2.3, 0.15, 48);
    const baseMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.3, metalness: 0.8 });
    const baseMesh = new THREE.Mesh(baseGeo, baseMat);
    baseMesh.position.y = -0.075;
    mMeshGroup.add(baseMesh);

    // Glowing Neon Ring
    const ringGeo = new THREE.TorusGeometry(2.25, 0.03, 16, 48);
    const ringMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
    const ringMesh = new THREE.Mesh(ringGeo, ringMat);
    ringMesh.rotation.x = Math.PI / 2;
    ringMesh.position.y = 0.02;
    mMeshGroup.add(ringMesh);

    setupDragAndDrop();
    animateModal();
  }

  function updateModalMesh(item) {
    if (!mMeshGroup) return;
    currentProductItem = item;

    if (customGLBModel) {
      return; // Keep imported GLB if active
    }

    clearCurrentModel();

    const m = new THREE.Group();
    const pName = item.product;

    if (pName === 'ชีสเค้ก') {
      // 1. Ceramic Dessert Plate with rim
      const plateGeo = new THREE.CylinderGeometry(1.85, 1.5, 0.08, 48);
      const plateMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.15, metalness: 0.1 });
      const plate = new THREE.Mesh(plateGeo, plateMat);
      plate.position.y = 0.04;
      m.add(plate);

      // 2. Triangular Wedge Cake Slice
      const shape = new THREE.Shape();
      shape.moveTo(0, 0);
      shape.lineTo(1.6, -0.65);
      shape.quadraticCurveTo(1.75, 0, 1.6, 0.65);
      shape.lineTo(0, 0);

      const extrudeSettings = { depth: 0.8, bevelEnabled: true, bevelSegments: 3, steps: 1, bevelSize: 0.04, bevelThickness: 0.04 };
      const sliceGeo = new THREE.ExtrudeGeometry(shape, extrudeSettings);
      sliceGeo.center();

      // Graham Cracker Crust (Bottom)
      const crustMat = new THREE.MeshStandardMaterial({ color: 0x9a5a2a, roughness: 0.8 });
      const crust = new THREE.Mesh(sliceGeo, crustMat);
      crust.scale.set(1.02, 1.02, 0.25);
      crust.rotation.x = Math.PI / 2;
      crust.position.set(0, 0.16, 0);
      m.add(crust);

      // Cream Cheese Body (Middle)
      const cheeseMat = new THREE.MeshStandardMaterial({ color: 0xfffae8, roughness: 0.3 });
      const cheese = new THREE.Mesh(sliceGeo, cheeseMat);
      cheese.scale.set(1, 1, 0.7);
      cheese.rotation.x = Math.PI / 2;
      cheese.position.set(0, 0.52, 0);
      m.add(cheese);

      // Strawberry Glaze (Top)
      const glazeMat = new THREE.MeshStandardMaterial({ color: 0xd91e36, roughness: 0.1, metalness: 0.2 });
      const glaze = new THREE.Mesh(sliceGeo, glazeMat);
      glaze.scale.set(1.01, 1.01, 0.1);
      glaze.rotation.x = Math.PI / 2;
      glaze.position.set(0, 0.85, 0);
      m.add(glaze);

      // Berry on Top
      const berryGeo = new THREE.DodecahedronGeometry(0.18, 1);
      const berryMat = new THREE.MeshStandardMaterial({ color: 0x990000, roughness: 0.2 });
      const berry = new THREE.Mesh(berryGeo, berryMat);
      berry.position.set(0.2, 0.98, 0);
      m.add(berry);

    } else if (pName === 'ลาเต้' || pName === 'คาปูชิโน' || pName === 'อเมริกาโน') {
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
      }

    } else if (pName === 'ครัวซองต์') {
      // 1. Ceramic Plate
      const plateGeo = new THREE.CylinderGeometry(1.75, 1.45, 0.08, 48);
      const plateMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.15, metalness: 0.1 });
      const plate = new THREE.Mesh(plateGeo, plateMat);
      plate.position.y = 0.04;
      m.add(plate);

      // 2. Crescent Croissant Body
      const croissantGroup = new THREE.Group();
      const segmentCount = 9;
      for (let i = 0; i < segmentCount; i++) {
        const t = (i / (segmentCount - 1)) - 0.5;
        const angle = t * Math.PI * 0.9;
        const radius = 1.0;
        const x = Math.sin(angle) * radius;
        const z = (Math.cos(angle) * radius * 0.65) - 0.5;
        
        const thickness = Math.cos(t * Math.PI) * 0.42 + 0.1;
        const segGeo = new THREE.SphereGeometry(thickness, 18, 18);
        segGeo.scale(1, 1.1, 1.35);

        const crustColor = (i % 2 === 0) ? 0xcc7722 : 0xd9822b;
        const segMat = new THREE.MeshStandardMaterial({ color: crustColor, roughness: 0.6 });
        const seg = new THREE.Mesh(segGeo, segMat);
        seg.position.set(x, 0.38 + thickness * 0.2, z);
        seg.rotation.y = -angle;
        croissantGroup.add(seg);
      }
      m.add(croissantGroup);

    } else if (pName === 'บราวนี') {
      // 1. Plate
      const plateGeo = new THREE.CylinderGeometry(1.65, 1.4, 0.08, 48);
      const plateMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.15 });
      const plate = new THREE.Mesh(plateGeo, plateMat);
      plate.position.y = 0.04;
      m.add(plate);

      // 2. Fudge Brownie Cube
      const brownieGeo = new THREE.BoxGeometry(1.3, 0.65, 1.3);
      const brownieMat = new THREE.MeshStandardMaterial({ color: 0x3d1c06, roughness: 0.75 });
      const brownie = new THREE.Mesh(brownieGeo, brownieMat);
      brownie.position.y = 0.4;
      m.add(brownie);

      // 3. Chocolate Glaze Drizzle Top
      const glazeGeo = new THREE.BoxGeometry(1.32, 0.08, 1.32);
      const glazeMat = new THREE.MeshStandardMaterial({ color: 0x241103, roughness: 0.2, metalness: 0.3 });
      const glaze = new THREE.Mesh(glazeGeo, glazeMat);
      glaze.position.y = 0.75;
      m.add(glaze);

      // 4. Roasted Walnut chips
      for (let i = 0; i < 5; i++) {
        const nutGeo = new THREE.DodecahedronGeometry(0.09);
        const nutMat = new THREE.MeshStandardMaterial({ color: 0xc19a6b, roughness: 0.6 });
        const nut = new THREE.Mesh(nutGeo, nutMat);
        nut.position.set((Math.random() - 0.5) * 0.75, 0.82, (Math.random() - 0.5) * 0.75);
        m.add(nut);
      }

    } else {
      // Cold Beverages: ชาไทย, โกโก้
      const isThaiTea = (pName === 'ชาไทย');
      const liquidColor = isThaiTea ? 0xe65100 : 0x4a2c1d;

      // 1. Coaster Base
      const coasterGeo = new THREE.CylinderGeometry(1.2, 1.2, 0.06, 36);
      const coasterMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.4 });
      const coaster = new THREE.Mesh(coasterGeo, coasterMat);
      coaster.position.y = 0.03;
      m.add(coaster);

      // 2. Translucent Glass Body
      const glassGeo = new THREE.CylinderGeometry(0.85, 0.68, 1.85, 32);
      const glassMat = new THREE.MeshPhysicalMaterial({
        color: 0xffffff,
        transparent: true,
        opacity: 0.35,
        roughness: 0.05,
        metalness: 0.1,
        transmission: 0.85,
        ior: 1.5
      });
      const glass = new THREE.Mesh(glassGeo, glassMat);
      glass.position.y = 0.98;
      m.add(glass);

      // 3. Liquid inside
      const liqGeo = new THREE.CylinderGeometry(0.8, 0.64, 1.6, 32);
      const liqMat = new THREE.MeshStandardMaterial({ color: liquidColor, roughness: 0.2 });
      const liquid = new THREE.Mesh(liqGeo, liqMat);
      liquid.position.y = 0.88;
      m.add(liquid);

      // Milk froth on top
      const frothGeo = new THREE.CylinderGeometry(0.81, 0.81, 0.15, 32);
      const frothMat = new THREE.MeshStandardMaterial({ color: 0xfffbeb, roughness: 0.3 });
      const froth = new THREE.Mesh(frothGeo, frothMat);
      froth.position.y = 1.68;
      m.add(froth);

      // 4. Floating Ice Cubes
      const iceGeo = new THREE.BoxGeometry(0.35, 0.35, 0.35);
      const iceMat = new THREE.MeshPhysicalMaterial({ color: 0xffffff, transparent: true, opacity: 0.7, roughness: 0.1, transmission: 0.9 });
      
      const ice1 = new THREE.Mesh(iceGeo, iceMat);
      ice1.position.set(0.15, 1.72, 0.1);
      ice1.rotation.set(0.3, 0.4, 0.2);
      m.add(ice1);

      const ice2 = new THREE.Mesh(iceGeo, iceMat);
      ice2.position.set(-0.2, 1.7, -0.15);
      ice2.rotation.set(0.1, 0.8, 0.3);
      m.add(ice2);

      // 5. Drinking Straw
      const strawColor = isThaiTea ? 0x38bdf8 : 0x10b981;
      const strawGeo = new THREE.CylinderGeometry(0.04, 0.04, 2.3, 16);
      const strawMat = new THREE.MeshStandardMaterial({ color: strawColor, roughness: 0.3 });
      const straw = new THREE.Mesh(strawGeo, strawMat);
      straw.position.set(0.2, 1.4, 0);
      straw.rotation.z = -0.22;
      straw.rotation.x = 0.15;
      m.add(straw);
    }

    mMeshGroup.add(m);
  }'''

assert old_three_engine in content, "old_three_engine not found!"
content = content.replace(old_three_engine, new_three_engine, 1)
print("Step 6: Replaced 3D engine with studio procedural models & GLTF support")

# Also update openProductModal to reset custom model when opening a new product
old_open_modal = '''  function openProductModal(prodName) {
    const item = PRODUCT_DATA[prodName];
    if (!item) return;'''

new_open_modal = '''  function openProductModal(prodName) {
    const item = PRODUCT_DATA[prodName];
    if (!item) return;

    // Reset imported GLB state for new product view
    customGLBModel = null;
    const btnReset = document.getElementById('btnResetModel');
    if (btnReset) btnReset.style.display = 'none';
    const badge = document.getElementById('modelModeBadge');
    if (badge) {
      badge.innerHTML = '<span class="i" style="font-size:12px;">auto_awesome</span> โมเดล 3D สมจริง (Studio)';
      badge.style.borderColor = 'rgba(56,189,248,.3)';
      badge.style.color = 'var(--cyan)';
    }'''

assert old_open_modal in content, "old_open_modal not found!"
content = content.replace(old_open_modal, new_open_modal, 1)
print("Step 7: Updated openProductModal to handle model reset")

# Write updated build_upgraded_html.py
with open(r'02_Labs_Assignments\auction-quad-dashboard\build_upgraded_html.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nSUCCESS: Updated build_upgraded_html.py!")
