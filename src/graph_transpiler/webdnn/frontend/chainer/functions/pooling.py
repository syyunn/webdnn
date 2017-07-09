import chainer.computational_graph

from webdnn.frontend.chainer.converter import ChainerConverter
from webdnn.graph.operators.average_pooling_2d import AveragePooling2D
from webdnn.graph.operators.max_pooling_2d import MaxPooling2D


@ChainerConverter.register_handler("AveragePooling2D")
def _convert_average_pooling2d(converter: ChainerConverter, c_op: chainer.functions.AveragePooling2D):
    x = converter.get_variable(c_op.inputs[0])

    pool_opr = AveragePooling2D(None,
                                ksize=(c_op.kh, c_op.kw),
                                stride=(c_op.sy, c_op.sx),
                                padding=(c_op.ph, c_op.pw))

    y, = pool_opr(x)

    converter.set_variable(c_op.outputs[0](), y)


# noinspection PyUnusedLocal
@ChainerConverter.register_handler("AveragePoolingND")
def _convert_average_pooling_nd(converter: ChainerConverter, c_op: chainer.functions.AveragePoolingND):
    # TODO
    raise NotImplementedError("[ChainerConverter] AveragePoolingND is not supported")


@ChainerConverter.register_handler("MaxPooling2D")
def _convert_max_pooling2d(converter: ChainerConverter, c_op: chainer.functions.MaxPooling2D):
    if not c_op.cover_all:
        raise NotImplementedError("'cover_all=False' property in 'MaxPooling2D' is not supported.")

    x = converter.get_variable(c_op.inputs[0])

    pool_opr = MaxPooling2D(None,
                            ksize=(c_op.kh, c_op.kw),
                            stride=(c_op.sy, c_op.sx),
                            padding=(c_op.ph, c_op.pw))

    y, = pool_opr(x)

    converter.set_variable(c_op.outputs[0](), y)


# noinspection PyUnusedLocal
@ChainerConverter.register_handler("MaxPoolingND")
def _convert_max_pooling_nd(converter: ChainerConverter, c_op: chainer.functions.MaxPoolingND):
    # TODO
    raise NotImplementedError("[ChainerConverter] MaxPoolingND is not supported")


# noinspection PyUnusedLocal
@ChainerConverter.register_handler("ROIPooling2D")
def _convert_roi_pooling2d(converter: ChainerConverter, c_op: chainer.functions.ROIPooling2D):
    # TODO
    raise NotImplementedError("[ChainerConverter] ROIPooling2D is not supported")


# noinspection PyUnusedLocal
@ChainerConverter.register_handler("SpatialPyramidPooling2D")
def _convert_spatial_pyramid_pooling2d(converter: ChainerConverter, c_op: chainer.functions.SpatialPyramidPooling2D):
    # TODO
    raise NotImplementedError("[ChainerConverter] SpatialPyramidPooling2D is not supported")


# noinspection PyUnusedLocal
@ChainerConverter.register_handler("Unpooling2D")
def _convert_unpooling2d(converter: ChainerConverter, c_op: chainer.functions.Unpooling2D):
    # TODO
    raise NotImplementedError("[ChainerConverter] Unpooling2D is not supported")


# noinspection PyUnusedLocal
@ChainerConverter.register_handler("UnpoolingND")
def _convert_unpooling_nd(converter: ChainerConverter, c_op: chainer.functions.UnpoolingND):
    # TODO
    raise NotImplementedError("[ChainerConverter] UnpoolingND is not supported")


# noinspection PyUnusedLocal
@ChainerConverter.register_handler("Upsampling2D")
def _convert_upsampling2d(converter: ChainerConverter, c_op: chainer.functions.Upsampling2D):
    # TODO
    raise NotImplementedError("[ChainerConverter] Upsampling2D is not supported")