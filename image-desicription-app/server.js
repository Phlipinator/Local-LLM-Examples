const express = require('express');
const multer = require('multer');
const path = require('path');
const { LMStudioClient } = require('@lmstudio/sdk');

const app = express();
const PORT = 3000;

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/');
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + path.extname(file.originalname));
  }
});

const upload = multer({ storage: storage });
app.use(express.static('public'));

// New route that uploads AND describes the image
app.post('/describe', upload.single('image'), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: 'No file uploaded' });
    }
    
    console.log('Processing image:', req.file.filename);
    
    // Your LLM code goes here
    const client = new LMStudioClient();
    const model = await client.llm.model("qwen2-vl-2b-instruct");
    
    const imagePath = req.file.path; // This is the uploaded file path
    const image = await client.files.prepareImage(imagePath);
    
    const prediction = await model.respond([
      { role: "user", content: "Describe this image please", images: [image] },
    ]);
    
    res.json({ 
      description: prediction.content,
      filename: req.file.filename 
    });
    
  } catch (error) {
    console.error('Error describing image:', error);
    res.status(500).json({ error: 'Failed to describe image' });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});