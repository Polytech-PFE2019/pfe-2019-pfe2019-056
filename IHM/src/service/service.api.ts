import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Observable} from 'rxjs';


@Injectable()
export  class ServiceApi {

  public respnseUpload
  public respnseConflicts
  public responseData
  public responsInstance

  constructor(private http:HttpClient){
  }

  public getResult(request) {

    return this.responseData=this.http.post<any>("http://localhost:5000/queering/",request)

  }

  public getInstance(Instances) {

    return this.http.post<any>("http://localhost:5000/add_instance/",Instances);

  }

  public getConflicts() {

    return this.http.get<any>("http://localhost:5000/conflicts/")


  }

  public getAcm(Conflict) {

    return this.http.get("http://localhost:5000/ACM?conflict="+Conflict);

  }



  //public post(file:File):Observable<any> {
    //const formData = new FormData();
    //formData.append('file', file, file.name);
    //return this.http.request('POSThis.ApiUrl, { body:formData });
  //}

}
