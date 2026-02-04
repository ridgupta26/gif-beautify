// Global variables
let selectedFiles = []; // Changed to array for multiple files
let currentFilenames = []; // Array to store processed filenames
let currentPreviewIndex = 0; // Track which file is being previewed
let backgroundType = 'gradient'; // 'gradient' or 'image'
let backgroundImageUrl = null;

// DOM elements
const settingsSection = document.getElementById('settingsSection');
const resultSection = document.getElementById('resultSection');
const loadingOverlay = document.getElementById('loadingOverlay');

const fileInput = document.getElementById('fileInput');
const addFilesBtn = document.getElementById('addFilesBtn');
const fileUploadSidebar = document.getElementById('fileUploadSidebar');
const fileCount = document.getElementById('fileCount');

const preview = document.getElementById('preview');
const emptyPreview = document.getElementById('emptyPreview');
const fileInfo = document.getElementById('fileInfo');
const fileList = document.getElementById('fileList');
const compressBtnText = document.getElementById('compressBtnText');
const downloadAllBtn = document.getElementById('downloadAllBtn');
const batchResults = document.getElementById('batchResults');
const loadingProgress = document.getElementById('loadingProgress');

const targetSize = document.getElementById('targetSize');
const gifWidth = document.getElementById('gifWidth');
const resetBtn = document.getElementById('resetBtn');
const compressBtn = document.getElementById('compressBtn');
const downloadBtn = document.getElementById('downloadBtn');
const newFileBtn = document.getElementById('newFileBtn');

const resultStats = document.getElementById('resultStats');

// Hidden inputs for actual values
const borderRadius = document.getElementById('borderRadius');
const offsetX = document.getElementById('offsetX');
const shadowSize = document.getElementById('shadowSize');
const addBackground = document.getElementById('addBackground');
const backgroundSettings = document.getElementById('backgroundSettings');

// Hidden inputs for gradient colors (set by presets)
let gradientStart = '#667eea';
let gradientEnd = '#764ba2';

// Event Listeners
addFilesBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    fileInput.click();
});

fileInput.addEventListener('change', handleFileSelect);

// Drag and drop on the entire window
document.addEventListener('dragover', handleDragOver);
document.addEventListener('dragleave', handleDragLeave);
document.addEventListener('drop', handleDrop);

// Preset button handlers for target size
document.querySelectorAll('#targetSizeButtons .preset-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        document.querySelectorAll('#targetSizeButtons .preset-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        targetSize.value = this.dataset.value;
        document.getElementById('targetSizeCustom').value = '';
    });
});

// Custom target size input
document.getElementById('targetSizeCustom').addEventListener('input', function() {
    if (this.value) {
        document.querySelectorAll('#targetSizeButtons .preset-btn').forEach(b => b.classList.remove('active'));
        targetSize.value = this.value;
    }
});

// Preset button handlers for GIF width
document.querySelectorAll('#gifWidthButtons .preset-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        document.querySelectorAll('#gifWidthButtons .preset-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        gifWidth.value = this.dataset.value;
        document.getElementById('gifWidthCustom').value = '';
        updatePreview();
    });
});

// Custom GIF width input
document.getElementById('gifWidthCustom').addEventListener('input', function() {
    if (this.value) {
        document.querySelectorAll('#gifWidthButtons .preset-btn').forEach(b => b.classList.remove('active'));
        gifWidth.value = this.value;
        updatePreview();
    }
});

// Preset button handlers for rounded corners
document.querySelectorAll('#borderRadiusButtons .preset-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        // Remove active class from all buttons in this group
        document.querySelectorAll('#borderRadiusButtons .preset-btn').forEach(b => b.classList.remove('active'));
        
        // Add active class to clicked button
        this.classList.add('active');
        
        // Update hidden input value
        borderRadius.value = this.dataset.value;
        
        // Clear custom input
        document.getElementById('borderRadiusCustom').value = '';
        
        // Update preview
        updatePreview();
    });
});

// Custom border radius input
document.getElementById('borderRadiusCustom').addEventListener('input', function() {
    if (this.value) {
        // Remove active class from all preset buttons
        document.querySelectorAll('#borderRadiusButtons .preset-btn').forEach(b => b.classList.remove('active'));
        
        // Update hidden input value
        borderRadius.value = this.value;
        
        // Update preview
        updatePreview();
    }
});

// Preset button handlers for padding
document.querySelectorAll('#paddingButtons .preset-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        // Remove active class from all buttons in this group
        document.querySelectorAll('#paddingButtons .preset-btn').forEach(b => b.classList.remove('active'));
        
        // Add active class to clicked button
        this.classList.add('active');
        
        // Update hidden input value
        offsetX.value = this.dataset.value;
        
        // Clear custom input
        document.getElementById('paddingCustom').value = '';
        
        // Update preview
        updatePreview();
    });
});

// Custom padding input
document.getElementById('paddingCustom').addEventListener('input', function() {
    if (this.value) {
        // Remove active class from all preset buttons
        document.querySelectorAll('#paddingButtons .preset-btn').forEach(b => b.classList.remove('active'));
        
        // Update hidden input value
        offsetX.value = this.value;
        
        // Update preview
        updatePreview();
    }
});

// Preset button handlers for shadow
document.querySelectorAll('#shadowButtons .preset-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        // Remove active class from all buttons in this group
        document.querySelectorAll('#shadowButtons .preset-btn').forEach(b => b.classList.remove('active'));
        
        // Add active class to clicked button
        this.classList.add('active');
        
        // Update hidden input value
        shadowSize.value = this.dataset.value;
        
        // Update preview
        updatePreview();
    });
});

// Background preset and wallpaper selection
document.querySelectorAll('.preset-item').forEach(preset => {
    preset.addEventListener('click', function() {
        // Remove active class from all items
        document.querySelectorAll('.preset-item').forEach(p => p.classList.remove('active'));
        
        // Add active class to clicked preset
        this.classList.add('active');
        
        // Check if it's a gradient or image
        if (this.dataset.type === 'image') {
            // Image wallpaper
            backgroundType = 'image';
            backgroundImageUrl = this.dataset.url;
            gradientStart = '#ffffff';
            gradientEnd = '#ffffff';
        } else {
            // Gradient
            backgroundType = 'gradient';
            gradientStart = this.dataset.start;
            gradientEnd = this.dataset.end;
            backgroundImageUrl = null;
        }
        
        // Update preview
        updatePreview();
    });
});

addBackground.addEventListener('change', (e) => {
    backgroundSettings.style.display = e.target.checked ? 'block' : 'none';
    updatePreview();
});

resetBtn.addEventListener('click', handleReset);
compressBtn.addEventListener('click', handleCompress);
downloadBtn.addEventListener('click', handleDownload);
downloadAllBtn.addEventListener('click', handleDownloadAll);
newFileBtn.addEventListener('click', handleNewFile);

// Initialize UI state
document.addEventListener('DOMContentLoaded', function() {
    updateFileInfo(); // This will disable the compress button initially
});

// Functions
function updatePreview() {
    const previewImg = document.getElementById('preview');
    const previewContainer = document.getElementById('previewContainer');
    const previewWrapper = document.getElementById('previewWrapper');
    
    if (!previewImg.src || previewImg.src === '') return;
    
    // Get current settings
    const radius = parseInt(borderRadius.value);
    const padding = parseInt(offsetX.value);
    const shadow = shadowSize.value;
    const hasBackground = addBackground.checked;
    
    // Apply border radius to image
    previewImg.style.borderRadius = `${radius}px`;
    
    // Apply shadow to image based on size
    let shadowStyle = 'none';
    if (shadow === 'small') {
        shadowStyle = '0 4px 6px rgba(0, 0, 0, 0.1), 0 2px 4px rgba(0, 0, 0, 0.06)';
    } else if (shadow === 'medium') {
        shadowStyle = '0 10px 15px rgba(0, 0, 0, 0.3), 0 4px 6px rgba(0, 0, 0, 0.2)';
    } else if (shadow === 'large') {
        shadowStyle = '0 20px 25px rgba(0, 0, 0, 0.4), 0 10px 10px rgba(0, 0, 0, 0.3)';
    }
    previewImg.style.boxShadow = shadowStyle;
    
    // Apply exact padding and background to wrapper (this is what gets exported)
    if (hasBackground) {
        // Apply background based on type
        if (backgroundType === 'image' && backgroundImageUrl) {
            previewWrapper.style.background = `url(${backgroundImageUrl})`;
            previewWrapper.style.backgroundSize = 'cover';
            previewWrapper.style.backgroundPosition = 'center';
        } else {
            // Create gradient background on wrapper
            if (gradientStart === gradientEnd) {
                previewWrapper.style.background = gradientStart;
            } else {
                previewWrapper.style.background = `linear-gradient(135deg, ${gradientStart} 0%, ${gradientEnd} 100%)`;
            }
            previewWrapper.style.backgroundSize = 'auto';
        }
        // Apply exact padding to wrapper - this is the actual export padding
        previewWrapper.style.padding = `${padding}px`;
        // Container stays dark
        previewContainer.style.background = '#1a1a1a';
    } else {
        // No background - show GIF on dark background with no padding
        previewWrapper.style.background = 'transparent';
        previewWrapper.style.padding = '0';
        previewContainer.style.background = '#1a1a1a';
    }
}
function isValidHex(hex) {
    return /^#[0-9A-F]{6}$/i.test(hex);
}

function handleDragOver(e) {
    e.preventDefault();
    fileUploadSidebar.classList.add('drag-over');
}

function handleDragLeave(e) {
    e.preventDefault();
    // Only remove if leaving the window
    if (e.target === document) {
        fileUploadSidebar.classList.remove('drag-over');
    }
}

function handleDrop(e) {
    e.preventDefault();
    fileUploadSidebar.classList.remove('drag-over');
    
    const files = Array.from(e.dataTransfer.files);
    if (files.length > 0) {
        handleFiles(files);
    }
}

function handleFileSelect(e) {
    e.stopPropagation();
    const files = Array.from(e.target.files);
    if (files.length > 0) {
        console.log(`${files.length} file(s) selected`);
        handleFiles(files);
    } else {
        console.log('No files selected');
    }
    // Don't reset file input so users can add more files
}

function handleFiles(files) {
    console.log('handleFiles called with:', files.length, 'files');
    
    // Check if adding would exceed 10 files
    const totalFiles = selectedFiles.length + files.length;
    if (totalFiles > 10) {
        const allowed = 10 - selectedFiles.length;
        if (allowed <= 0) {
            alert('Maximum 10 files allowed. Please remove some files first.');
            return;
        }
        alert(`Maximum 10 files allowed. Only adding the first ${allowed} file(s).`);
        files = files.slice(0, allowed);
    }
    
    // Filter for GIF files only
    const gifFiles = files.filter(file => file.type.includes('gif'));
    
    if (gifFiles.length === 0) {
        alert('Please select only GIF files');
        return;
    }
    
    if (gifFiles.length < files.length) {
        alert(`${files.length - gifFiles.length} non-GIF file(s) were skipped`);
    }
    
    // Add to existing files
    selectedFiles = [...selectedFiles, ...gifFiles];
    console.log('Total GIF files:', selectedFiles.length);
    
    // Update file count badge
    fileCount.textContent = selectedFiles.length;
    
    // Always show file list in sidebar
    renderFileList();
    
    // Update button text
    if (selectedFiles.length > 1) {
        compressBtnText.textContent = `Export ${selectedFiles.length} GIFs`;
    } else {
        compressBtnText.textContent = 'Export GIF(s)';
    }
    
    // Show preview of last added file
    currentPreviewIndex = selectedFiles.length - 1;
    showFilePreview(currentPreviewIndex);
    
    // Update file info
    updateFileInfo();
}

function updateFileInfo() {
    const totalSizeMB = selectedFiles.reduce((sum, f) => sum + f.size, 0) / (1024 * 1024);
    
    // Enable/disable compress button
    const compressBtn = document.getElementById('compressBtn');
    compressBtn.disabled = selectedFiles.length === 0;
    
    // Update file count badge
    fileCount.textContent = selectedFiles.length;
    
    if (selectedFiles.length === 0) {
        fileInfo.innerHTML = '<span style="color: var(--text-secondary);">No file selected</span>';
    } else if (selectedFiles.length === 1) {
        const sizeMB = (selectedFiles[0].size / (1024 * 1024)).toFixed(2);
        fileInfo.innerHTML = `
            <span><strong>${selectedFiles[0].name}</strong></span>
            <span>${sizeMB} MB</span>
        `;
    } else {
        fileInfo.innerHTML = `
            <span><strong>${selectedFiles.length} files</strong></span>
            <span>${totalSizeMB.toFixed(2)} MB total</span>
        `;
    }
    fileInfo.style.display = 'flex';
    fileInfo.style.gap = '1rem';
}

function renderFileList() {
    if (selectedFiles.length === 0) {
        fileList.innerHTML = `
            <div class="empty-files-message">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                    <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"></path>
                    <polyline points="13 2 13 9 20 9"></polyline>
                </svg>
                <p>No files yet</p>
            </div>
        `;
        return;
    }
    
    fileList.innerHTML = '';
    selectedFiles.forEach((file, index) => {
        const sizeMB = (file.size / (1024 * 1024)).toFixed(2);
        const item = document.createElement('div');
        item.className = 'file-list-item' + (index === currentPreviewIndex ? ' active' : '');
        item.innerHTML = `
            <span class="file-list-item-name" title="${file.name}">${file.name}</span>
            <span class="file-list-item-size">${sizeMB} MB</span>
            <button class="file-list-item-remove" onclick="removeFile(${index}); event.stopPropagation();">×</button>
        `;
        item.onclick = () => showFilePreview(index);
        fileList.appendChild(item);
    });
}

function removeFile(index) {
    selectedFiles.splice(index, 1);
    
    if (selectedFiles.length === 0) {
        // Reset to empty state
        currentPreviewIndex = 0;
        preview.style.display = 'none';
        emptyPreview.style.display = 'flex';
        compressBtnText.textContent = 'Export GIF(s)';
        renderFileList(); // Show empty state
        updateFileInfo();
        return;
    }
    
    // Update preview index if needed
    if (currentPreviewIndex >= selectedFiles.length) {
        currentPreviewIndex = selectedFiles.length - 1;
    }
    
    // Re-render list and preview
    renderFileList();
    
    // Update button text
    if (selectedFiles.length > 1) {
        compressBtnText.textContent = `Export ${selectedFiles.length} GIFs`;
    } else {
        compressBtnText.textContent = 'Export GIF(s)';
    }
    
    showFilePreview(currentPreviewIndex);
    updateFileInfo();
}

function showFilePreview(index) {
    currentPreviewIndex = index;
    const file = selectedFiles[index];
    
    // Update active state in file list
    document.querySelectorAll('.file-list-item').forEach((item, i) => {
        if (i === index) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }
    });
    
    // Load preview
    const reader = new FileReader();
    reader.onload = (e) => {
        console.log('File loaded successfully for preview');
        preview.src = e.target.result;
        preview.style.display = 'block';
        emptyPreview.style.display = 'none';
        setTimeout(updatePreview, 100);
    };
    reader.onerror = (e) => {
        console.error('Error reading file:', e);
        alert('Error reading file. Please try again.');
    };
    reader.readAsDataURL(file);
}

function handleReset() {
    // Reset target size to 5 MB
    targetSize.value = 5;
    document.querySelectorAll('#targetSizeButtons .preset-btn').forEach(b => b.classList.remove('active'));
    document.querySelector('#targetSizeButtons .preset-btn[data-value="5"]').classList.add('active');
    document.getElementById('targetSizeCustom').value = '';
    
    // Reset GIF width to 1920
    gifWidth.value = 1920;
    document.querySelectorAll('#gifWidthButtons .preset-btn').forEach(b => b.classList.remove('active'));
    document.querySelector('#gifWidthButtons .preset-btn[data-value="1920"]').classList.add('active');
    document.getElementById('gifWidthCustom').value = '';
    
    // Reset border radius to 8
    borderRadius.value = 8;
    document.querySelectorAll('#borderRadiusButtons .preset-btn').forEach(b => b.classList.remove('active'));
    document.querySelector('#borderRadiusButtons .preset-btn[data-value="8"]').classList.add('active');
    document.getElementById('borderRadiusCustom').value = '';
    
    // Reset padding to 80
    offsetX.value = 80;
    document.querySelectorAll('#paddingButtons .preset-btn').forEach(b => b.classList.remove('active'));
    document.querySelector('#paddingButtons .preset-btn[data-value="80"]').classList.add('active');
    document.getElementById('paddingCustom').value = '';
    
    // Reset shadow to none (no shadow by default)
    shadowSize.value = '0';
    document.querySelectorAll('#shadowButtons .preset-btn').forEach(b => b.classList.remove('active'));
    document.querySelector('#shadowButtons .preset-btn[data-value="0"]').classList.add('active');
    
    addBackground.checked = true;
    backgroundSettings.style.display = 'block';
    
    // Reset to first gradient preset
    document.querySelectorAll('.preset-item').forEach(p => p.classList.remove('active'));
    document.querySelector('.preset-item').classList.add('active');
    backgroundType = 'gradient';
    gradientStart = '#667eea';
    gradientEnd = '#764ba2';
    backgroundImageUrl = null;
    
    // Update preview
    updatePreview();
}

async function handleCompress() {
    if (selectedFiles.length === 0) return;
    
    // Show loading and disable button
    loadingOverlay.style.display = 'flex';
    compressBtn.disabled = true;
    
    currentFilenames = [];
    const results = [];
    
    // Process each file
    for (let i = 0; i < selectedFiles.length; i++) {
        const file = selectedFiles[i];
        loadingProgress.textContent = `Processing ${i + 1} of ${selectedFiles.length}: ${file.name}`;
        
        // Prepare form data
        const formData = new FormData();
        formData.append('file', file);
        formData.append('targetSize', targetSize.value);
        formData.append('gifWidth', gifWidth.value);
        formData.append('borderRadius', borderRadius.value);
        formData.append('shadowSize', shadowSize.value);
        formData.append('backgroundType', backgroundType);
        
        if (backgroundType === 'image' && backgroundImageUrl) {
            formData.append('backgroundImageUrl', backgroundImageUrl);
        } else {
            formData.append('gradientStart', gradientStart);
            formData.append('gradientEnd', gradientEnd);
        }
        
        formData.append('offsetX', offsetX.value);
        formData.append('offsetY', offsetX.value); // Using same value for both X and Y
        formData.append('addBackground', addBackground.checked);
        
        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            
            if (data.success) {
                currentFilenames.push(data.filename);
                results.push({
                    success: true,
                    filename: data.filename,
                    originalName: file.name,
                    ...data
                });
            } else {
                results.push({
                    success: false,
                    originalName: file.name,
                    error: data.error
                });
            }
        } catch (error) {
            results.push({
                success: false,
                originalName: file.name,
                error: error.message
            });
        }
    }
    
    loadingOverlay.style.display = 'none';
    compressBtn.disabled = false;  // Re-enable button
    
    // Show results
    if (selectedFiles.length === 1) {
        // Single file - show traditional result
        if (results[0].success) {
            showResults(results[0]);
        } else {
            alert(`Error: ${results[0].error}`);
        }
    } else {
        // Multiple files - show batch results
        showBatchResults(results);
    }
}

function showResults(data) {
    const originalMB = (data.original_size / (1024 * 1024)).toFixed(2);
    const compressedMB = (data.compressed_size / (1024 * 1024)).toFixed(2);
    const reduction = data.reduction.toFixed(1);
    
    resultStats.innerHTML = `
        <div class="stat-item">
            <span class="stat-label">Original Size</span>
            <span class="stat-value">${originalMB} MB</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">Compressed Size</span>
            <span class="stat-value success">${compressedMB} MB</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">Size Reduction</span>
            <span class="stat-value success">${reduction}%</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">Strategy Used</span>
            <span class="stat-value">${data.strategy}</span>
        </div>
    `;
    
    resultStats.style.display = 'block';
    batchResults.style.display = 'none';
    downloadBtn.style.display = 'inline-flex';
    downloadAllBtn.style.display = 'none';
    document.getElementById('resultTitle').textContent = 'Compression Complete!';
    
    // Hide header compress button
    compressBtn.style.display = 'none';
    
    // Switch to results view
    settingsSection.style.display = 'none';
    resultSection.style.display = 'flex';
}

function showBatchResults(results) {
    const successCount = results.filter(r => r.success).length;
    const totalOriginal = results.reduce((sum, r) => sum + (r.original_size || 0), 0);
    const totalCompressed = results.reduce((sum, r) => sum + (r.compressed_size || 0), 0);
    const totalReduction = totalOriginal > 0 ? ((totalOriginal - totalCompressed) / totalOriginal * 100).toFixed(1) : 0;
    
    // Show summary stats
    resultStats.innerHTML = `
        <div class="stat-item">
            <span class="stat-label">Files Processed</span>
            <span class="stat-value">${successCount} of ${results.length}</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">Total Original Size</span>
            <span class="stat-value">${(totalOriginal / (1024 * 1024)).toFixed(2)} MB</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">Total Compressed Size</span>
            <span class="stat-value success">${(totalCompressed / (1024 * 1024)).toFixed(2)} MB</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">Average Reduction</span>
            <span class="stat-value success">${totalReduction}%</span>
        </div>
    `;
    
    // Show individual results
    batchResults.innerHTML = '';
    results.forEach((result, index) => {
        const item = document.createElement('div');
        item.className = 'batch-result-item';
        
        if (result.success) {
            const originalMB = (result.original_size / (1024 * 1024)).toFixed(2);
            const compressedMB = (result.compressed_size / (1024 * 1024)).toFixed(2);
            const reduction = result.reduction.toFixed(1);
            
            item.innerHTML = `
                <div class="batch-result-header">
                    <span class="batch-result-name">${result.originalName}</span>
                    <span class="batch-result-status success">✓ Success</span>
                </div>
                <div class="batch-result-stats">
                    <span>${originalMB} MB → ${compressedMB} MB</span>
                    <span>•</span>
                    <span>${reduction}% reduction</span>
                </div>
                <div class="batch-result-download">
                    <button class="btn btn-secondary" onclick="downloadSingle('${result.filename}')">Download</button>
                </div>
            `;
        } else {
            item.innerHTML = `
                <div class="batch-result-header">
                    <span class="batch-result-name">${result.originalName}</span>
                    <span class="batch-result-status error">✗ Failed</span>
                </div>
                <div class="batch-result-stats">
                    <span style="color: var(--error);">${result.error}</span>
                </div>
            `;
        }
        
        batchResults.appendChild(item);
    });
    
    resultStats.style.display = 'block';
    batchResults.style.display = 'block';
    downloadBtn.style.display = 'none';
    downloadAllBtn.style.display = successCount > 0 ? 'inline-flex' : 'none';
    document.getElementById('resultTitle').textContent = `Batch Processing Complete!`;
    
    // Hide header compress button
    compressBtn.style.display = 'none';
    
    // Switch to results view
    settingsSection.style.display = 'none';
    resultSection.style.display = 'flex';
}

function downloadSingle(filename) {
    window.location.href = `/download/${filename}`;
}

function handleDownload() {
    if (currentFilenames.length === 1) {
        window.location.href = `/download/${currentFilenames[0]}`;
    }
}

async function handleDownloadAll() {
    if (currentFilenames.length === 0) return;
    
    // Create a form to submit filenames
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = '/download-batch';
    form.style.display = 'none';
    
    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'filenames';
    input.value = JSON.stringify(currentFilenames);
    
    form.appendChild(input);
    document.body.appendChild(form);
    form.submit();
    document.body.removeChild(form);
}

function handleNewFile() {
    // Reset everything
    selectedFiles = [];
    currentFilenames = [];
    currentPreviewIndex = 0;
    fileInput.value = '';
    preview.src = '';
    preview.style.display = 'none';
    preview.style.boxShadow = 'none';
    preview.style.borderRadius = '0';
    emptyPreview.style.display = 'flex';
    fileInfo.innerHTML = '<span style="color: var(--text-secondary);">No file selected</span>';
    fileCount.textContent = '0';
    renderFileList(); // Show empty state
    compressBtnText.textContent = 'Export GIF(s)';
    
    // Clear preview wrapper styling
    const previewWrapper = document.getElementById('previewWrapper');
    const previewContainer = document.getElementById('previewContainer');
    if (previewWrapper) {
        previewWrapper.style.background = 'transparent';
        previewWrapper.style.padding = '0';
        previewWrapper.style.backgroundSize = 'auto';
    }
    if (previewContainer) {
        previewContainer.style.background = '#1a1a1a';
    }
    
    // Show header compress button again
    compressBtn.style.display = 'inline-flex';
    
    // Reset settings
    handleReset();
    
    // Switch back to main view
    resultSection.style.display = 'none';
    settingsSection.style.display = 'grid';
    
    console.log('Reset to main view');
}


