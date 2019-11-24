from Camera import Camera
class Shop:
    def __init__(self, _id):
        self._id = _id
        self.dict_cameras = []
    
    def get_id(self):
        return self._id

    def get_camera(self, _id):
        i = 0
        for camera in self.dict_cameras:
            if (camera.get_id() == _id):
                return self.dict_cameras[i]
            i += 1
        return -1

    def get_cameras_id(self):
        ids = []
        for camera in self.dict_cameras:
            ids.append(camera.get_id())
        return ids

    def get_status(self):
        sum_density = 0
        for camera in self.dict_cameras:
            sum_density += camera.density
        return sum_density / len(self.dict_cameras)

    def get_count_cameras(self):
        return len(self.dict_cameras)
    
    def add_camera(self):
        new_id = len(self.dict_cameras)
        new_cam = Camera(new_id)
        self.dict_cameras.append(new_cam)
        return str(new_id)
        