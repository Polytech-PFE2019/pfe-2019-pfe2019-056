import { Component, OnInit } from '@angular/core';
import {ServiceApi} from '../../service/service.api';
import {Router} from '@angular/router';

@Component({
  selector: 'app-instance',
  templateUrl: './instance.component.html',
  styleUrls: ['./instance.component.css']
})
export class InstanceComponent implements OnInit {

  public  reponse

  instance= {
    user:"",
    Env:"",
    Act:""
  };


  constructor(private serviceApi:ServiceApi,private router:Router) { }

  ngOnInit() {
  }

  ngAfterViewInit(){

    this.reponse=this.serviceApi.responsInstance
    console.log(this.reponse)
  }

  onSubmit(f) {

    console.log(f['user'])
    console.log(f['Env'])
    console.log(f['Act'])

    const formData = new FormData();
    formData.append('user',f['user'])
    formData.append('environment',f['Env'])
    formData.append('activity',f['Act'])

    console.log(formData)

    this.serviceApi.getInstance(formData)
      .subscribe(data=>{
      this.reponse=data;
      console.log(this.reponse)
    },error => {
      console.log(error);
    })
   // this.router.navigate(['about']);

  }


}
