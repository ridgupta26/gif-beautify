# 🚀 Databricks App Deployment Guide - E2Dogfood Workspace

This guide will help you deploy the GIF Beautifier as a Databricks App on the E2Dogfood workspace.

## Prerequisites

- Databricks workspace access (E2Dogfood)
- Databricks CLI installed
- Valid Databricks authentication

---

## Step 1: Authenticate with E2Dogfood Workspace

Run this command to authenticate with E2Dogfood:

```bash
databricks auth login --host https://e2-dogfood.staging.cloud.databricks.com --profile e2dogfood
```

Or if your workspace URL is different, use:

```bash
databricks auth login --profile e2dogfood
```

The browser will open for you to complete authentication.

---

## Step 2: Sync the Project

Once authenticated, sync the project to your Databricks workspace:

```bash
cd /Users/ridhima.gupta/gif-compressor
databricks sync . /Workspace/Users/ridhima.gupta@databricks.com/gif-beautify --profile e2dogfood --full
```

---

## Step 3: Enable Watch Mode (Continuous Sync)

To automatically sync changes as you develop:

```bash
databricks sync --watch . /Workspace/Users/ridhima.gupta@databricks.com/gif-beautify --profile e2dogfood
```

Leave this running in a separate terminal while you work!

---

## Step 4: Create the Databricks App

### Option A: Using Databricks Workspace UI (Recommended)

1. Go to your E2Dogfood Databricks workspace
2. Navigate to **Apps** in the left sidebar
3. Click **Create App**
4. Configure:
   - **Name**: `gif-beautify`
   - **Source Path**: `/Workspace/Users/ridhima.gupta@databricks.com/gif-beautify`
   - **Command**: `python app.py` (automatically read from `app.yaml`)
5. Click **Create**

### Option B: Using Databricks CLI

```bash
databricks apps create gif-beautify \
  --source-code-path /Workspace/Users/ridhima.gupta@databricks.com/gif-beautify \
  --profile e2dogfood
```

---

## Configuration Files

### `app.yaml`

```yaml
command:
  - "python"
  - "app.py"
```

This tells Databricks Apps how to start your Flask application.

### `app.py` Updates

The following changes were made to support Databricks Apps:

```python
if __name__ == '__main__':
    # Get port from environment variable (Databricks Apps requirement)
    port = int(os.environ.get('PORT', 5000))
    # Bind to 0.0.0.0 for Databricks Apps
    app.run(host='0.0.0.0', port=port, debug=False)
```

---

## Accessing Your App

Once deployed, you can access your app at:

```
https://e2-dogfood.staging.cloud.databricks.com/apps/gif-beautify
```

Or check the **Apps** section in your Databricks workspace for the exact URL.

---

## Quick Command Reference - E2Dogfood

```bash
# Authenticate
databricks auth login --host https://e2-dogfood.staging.cloud.databricks.com --profile e2dogfood

# Full sync
databricks sync . /Workspace/Users/ridhima.gupta@databricks.com/gif-beautify --profile e2dogfood --full

# Watch mode (continuous sync)
databricks sync --watch . /Workspace/Users/ridhima.gupta@databricks.com/gif-beautify --profile e2dogfood

# Create app
databricks apps create gif-beautify --source-code-path /Workspace/Users/ridhima.gupta@databricks.com/gif-beautify --profile e2dogfood

# List apps
databricks apps list --profile e2dogfood

# View app details
databricks apps get gif-beautify --profile e2dogfood

# View app logs
databricks apps logs gif-beautify --profile e2dogfood
```

---

## Troubleshooting

### Authentication Issues

If you see authentication errors:

```bash
databricks auth login --host https://e2-dogfood.staging.cloud.databricks.com --profile e2dogfood
```

### Sync Issues

If files aren't syncing:

1. Check your `.gitignore` - make sure important files aren't excluded
2. Try a full sync: `databricks sync . <path> --full --profile e2dogfood`
3. Check file permissions

### App Not Starting

1. Check the app logs: `databricks apps logs gif-beautify --profile e2dogfood`
2. Verify `requirements.txt` includes all dependencies:
   ```
   Flask==3.0.0
   Pillow==10.1.0
   requests==2.31.0
   ```
3. Ensure `app.yaml` is in the root directory

### Port Issues

Databricks Apps automatically assign a port via the `PORT` environment variable. The app is configured to read this automatically.

---

## Manual Deployment Steps (Alternative)

If CLI doesn't work, you can manually deploy:

1. **Upload files to Databricks**:
   - Go to Workspace → Users → ridhima.gupta@databricks.com
   - Create folder: `gif-beautify`
   - Upload all files via UI

2. **Create App via UI**:
   - Navigate to Apps → Create App
   - Point to your workspace folder
   - Configure and deploy

---

## Next Steps

After deployment:

1. ✅ Test the app with a sample GIF
2. ✅ Share the app URL with your team
3. ✅ Monitor app logs for any issues
4. ✅ Update GitHub repo with deployment URL

---

## Support

For more information:
- [Databricks Apps Documentation](https://docs.databricks.com/en/dev-tools/databricks-apps/index.html)
- [Databricks CLI Documentation](https://docs.databricks.com/en/dev-tools/cli/index.html)

---

**Made with ❤️ for beautiful GIFs on Databricks E2Dogfood!**
