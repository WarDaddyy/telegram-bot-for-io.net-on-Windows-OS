import asyncio
import os
from aiogram import Bot, types
from aiodocker import Docker

TELEGRAM_TOKEN = 'TYPE_HERE_YOUR_TELEGRAM_TOKEN'

bot = Bot(token=TELEGRAM_TOKEN)
docker = Docker()

async def handle_update(update):
    """Function to handle incoming updates."""
    if update.message and update.message.text:
        if update.message.text.startswith('/status'):
            await send_docker_status(update.message.chat.id)

async def send_docker_status(chat_id):
    """Queries Docker container statuses and sends the result."""
    containers = await docker.containers.list(all=True)
    
    snippet = ""  # Copyable text snippet

    for container in containers:
        details = await container.show()
        status = details["State"]["Status"]
        container_id = container._id[:60]  # First 60 characters of container ID
        image_name = details['Config']['Image']
        snippet += f"- `{container_id}` ({image_name}): {status}\n"

    await bot.send_message(chat_id, snippet, parse_mode='Markdown')

async def send_docker_images_status(chat_id):
    """Queries Docker image statuses and sends the result."""
    message = "Docker Images Status:\n"
    images = await docker.images.list()

    for image in images:
        image_id = image['Id'][:12]  # First 12 characters of image ID
        tags = ', '.join(image['RepoTags'])
        message += f"- `{image_id}` ({tags}): Available\n"

    await bot.send_message(chat_id, message, parse_mode='Markdown')

async def remove_all_containers():
    """Function to remove all Docker containers."""
    try:
        containers = await docker.containers.list(all=True)
        for container in containers:
            await container.delete(force=True)
        return True
    except Exception as e:
        print(f"Container removal failed: {e}")
        return False

async def remove_all_images():
    """Function to remove all Docker images."""
    try:
        images = await docker.images.list()
        for image in images:
            await docker.images.delete(image['Id'])
        return True
    except Exception as e:
        print(f"Image removal failed: {e}")
        return False


async def restart_docker():
    """Function to restart the Docker service."""
    try:
        await docker.services.restart()
        return True
    except Exception as e:
        print(f"Docker restart failed: {e}")
        return False
    
SCRIPT_PATH = "TYPE_YOUR_SCRIPT_FILE_PATH_HERE"

async def run_powershell_script(script_path):
    """Function to execute the specified PowerShell script."""
    try:
        with open(script_path, 'r') as file:
            powershell_script = file.read()
            exec_command = f"powershell -Command \"{powershell_script}\""
            await os.system(exec_command)
        # PowerShell script execution başarılı olduğunda bilgilendirme mesajı gönder
        await bot.send_message(chat_id, "PowerShell script has been executed successfully.")
        return True
    except Exception as e:
        print(f"PowerShell script execution failed: {e}")
        return False


async def handle_update(update):
    """Function to handle incoming updates."""
    if update.message and update.message.text:
        if update.message.text.startswith('/status'):
            await send_docker_status(update.message.chat.id)
        elif update.message.text.startswith('/images_status'):
            await send_docker_images_status(update.message.chat.id)    
        elif update.message.text.startswith('/remove_container'):
            await remove_all_containers()
            await bot.send_message(update.message.chat.id, "All Docker containers have been removed.")
        elif update.message.text.startswith('/remove_image'):
            await remove_all_images()
            await bot.send_message(update.message.chat.id,"All Docker images have been removed.")
        elif update.message.text.startswith('/restart_docker'):
            await restart_docker()
            await bot.send_message(update.message.chat.id, "Docker service has been restarted.")
        elif update.message.text.startswith('/run_script'):
            await run_powershell_script(SCRIPT_PATH)
            await bot.send_message(update.message.chat.id, "PowerShell script has been executed successfully.")
        elif update.message.text.startswith('/menu'):
            await send_menu(update.message.chat.id)
        else:
            await bot.send_message(update.message.chat.id, "Invalid command. Please use a valid command.")

async def send_menu(chat_id):
    """Function to send the bot menu."""
    menu = "/status - Show Docker container statuses.\n" \
           "/images_status - Show Docker image statuses.\n" \
           "/remove_container - Remove all Docker containers.\n" \
           "/remove_image - Remove all Docker images.\n" \
           "/restart_docker - Restart the Docker service.\n" \
           "/run_script - Execute a pre-defined PowerShell script (re-run).\n"
    await bot.send_message(chat_id, menu)

async def main():
    """Main function of the bot to continuously poll for updates."""
    offset = None  # Offset to navigate between updates
    while True:
        updates = await bot.get_updates(offset=offset, timeout=20)
        for update in updates:
            await handle_update(update)
            offset = update.update_id + 1

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
