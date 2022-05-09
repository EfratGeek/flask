# flask
how do download file from python to client in local server.

in the client server , you need to call to the route.
# for example in react: 

import axios from "axios";
class FileService {

    get_exe_file() {
        // debugger
        return axios({
            url: 'http://127.0.0.1:5000//download',
            method: 'GET',
            responseType: 'blob',
        }).then((response) => {
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'file.exe');
            document.body.appendChild(link);
            console.log(link)
            link.click();
        });
    }
}
export default new FileService

# and in other page:

export default function Download() {
    const downloadFile = () => {
       fileService.get_exe_file()
    }
    return (
        <div>
          <button className='button-download' onClick={downloadFile}>download</button>
        </div>
    );
}


now you can use in this button , and this will download for you a file.


installs: 
pip install flask
pip install flask[async]
pip install -U flask-cors \ pip install flask-cors
