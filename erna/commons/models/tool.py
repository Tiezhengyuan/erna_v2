from django.db import models
from django.conf import settings
import os

class ToolManager(models.Manager):
    def tools_list(self):
        tools = {}
        for tool_obj in self.model.objects.all():
            name = tool_obj.tool_name
            version = tool_obj.version
            if name in tools:
                tools[name].append(version)
            else:
                tools[name] = [version,]
        return tools
    
    def get_last_version(self, tool_name):
        return  self.model.objects.filter(tool_name=tool_name).last()

    def get_tool(self, tool_name, version):
        try:
            tool_obj = self.model.objects.get(
                tool_name=tool_name, version=version)
            return tool_obj
        except Exception as e:
            pass
        return None


class Tool(models.Model):
    # required
    tool_name = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    tool_path = models.CharField(max_length=256)
    # optional
    default_parameters = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='default parameters of the tool'
    )
    create_time = models.DateTimeField(auto_now_add=True)
    download_url = models.CharField(max_length=1256, blank=True)

    objects = ToolManager()

    class Meta:
        app_label = 'commons'
        ordering = ['tool_name', 'version']
    
    
    def __str__(self):
        return self.tool_name
    
    @property
    def working_dir(self):
        return getattr(settings, 'TOOLS_DIR', None)

    @property
    def full_tool_path(self):
        return os.path.join(self.working_dir, self.tool_path)

    def add_tool(self, tool_info:dict):
        '''
        new tool would be added
        '''
        if 'tool_name' not in tool_info:
            raise ValueError('Name of the tool should be defined')
        if 'tool_path' not in tool_info:
            raise ValueError('path of the tool should be defined')
        dup = Tool.objects.filter(
            tool_name=tool_info['tool_name'],
            version=tool_info['version']
        )
        if len(dup) > 0:
            raise ValueError('duplicate on the name and version')
        # post a new tool
        tool_obj = Tool.objects.create(**tool_info)
        return tool_obj