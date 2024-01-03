
import open3d as o3d
import numpy as np

from pathlib import Path

basedir = Path("D:/baiduyun/tiab")


for scene in list((basedir).glob("*")):
    mesh1 = o3d.io.read_triangle_mesh(str(scene / "middle.ply"))
    mesh2 = o3d.io.read_triangle_mesh(str(scene / "mesh.glb"))

    print(scene)

    text = f"""

    
middle.ply
色彩 顶点色 sRGB
{np.asarray(mesh1.vertices).shape[0]:,} 顶点
{np.asarray(mesh1.triangles).shape[0]:,} 面

mesh.glb
4k PBR材质 符合 glTF 2.0 规范
{np.asarray(mesh2.vertices).shape[0]:,} 顶点
{np.asarray(mesh2.triangles).shape[0]:,} 面

下载链接 
链接：https://pan.baidu.com/s/1mJhmR-bl8APD36QWYUvKAA?pwd=jtji 
提取码：jtji
    """
    print(text)

    print("="*80)