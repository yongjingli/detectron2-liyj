# 1. 安装
# https://detectron2.readthedocs.io/en/latest/tutorials/install.html
# python -m pip install -e detectron2
# 但是最多只支持cuda-11.3, 需要修改本机的cuda后进行安装如修改为11.1
# 编译安装完成后可以将11.1 修改会 11.6 也不会报错

# 2. High Quality Entity Segmentation
# https://github.com/qqlu/Entity/blob/main/Entityv2/README.md
# https://github.com/qqlu/Entity 将这部分的代码加到detectron中
# https://github.com/qqlu/Entity/blob/main/Entityv2/CODE.md 将部分代码加入到project
# cd /XXX
# sudo python -m pip install -e detectron2
# cd detectron2
# cp -r /path/to/CropFormer projects/CropFormer
# cd projects/CropFormer/entity_api/PythonAPI
# sudo make
# cd ../../../..
# cd projects/CropFormer/mask2former/modeling/pixel_decoder/ops
# sudo sh make.sh

# OOM 显存不足
# python projects/CropFormer/demo_cropformer/demo_from_dirs.py --config-file /home/pxn-lyj/Egolee/programs/detectron2-liyj/projects/CropFormer/configs/entityv2/entity_segmentation/cropformer_swin_tiny_3x.yaml  --input /home/pxn-lyj/Egolee/data/test/mesh_jz/colors/*.jpg --output ./tmp_vis/  --opts MODEL.WEIGHTS /home/pxn-lyj/Downloads/CropFormer_swin_tiny_3x_5cea5e.pth

# 3.Open-World Entity Segmentation
# 采用卷积的模型
# https://github.com/qqlu/Entity/blob/main/Entity/README.md
#  python projects/EntitySeg/demo_result_and_vis.py --config-file /home/pxn-lyj/Egolee/programs/detectron2-liyj/projects/EntitySeg/configs/entity_r50_3x.yaml --input /home/pxn-lyj/Egolee/data/test/mesh_jz/colors/*.jpg --output /home/pxn-lyj/Egolee/data/test/mesh_jz/model_output MODEL.WEIGHTS /home/pxn-lyj/Egolee/programs/detectron2-liyj/weights/ours_R50_3x.pth MODEL.CONDINST.MASK_BRANCH.USE_MASK_RESCORE "True"

# 4. 进行onnx的导出
# from caffe2.proto import caffe2_pb2 as _tmp
# TypeError: Descriptors cannot be created directly.
# libprotoc 3.6.1 将protoc的版本升级
# pip install protobuf==3.19.0
