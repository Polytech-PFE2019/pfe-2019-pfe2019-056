import { FormBuilder, FormGroup } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import {Component, OnInit} from '@angular/core';
import {ServiceApi} from '../../service/service.api';
import {Router} from '@angular/router';

@Component({
  selector: 'app-formulaire',
  templateUrl: './formulaire.component.html',
  styleUrls: ['./formulaire.component.css']
})
export class FormulaireComponent implements OnInit {

  public mode=1
  public response
  public responseupload
  SERVER_URL = "http://localhost:5000/upload/";

  uploadForm: FormGroup;

  constructor(private formBuilder: FormBuilder, private httpClient: HttpClient,
              private serviceApi:ServiceApi,private router:Router) {
  }

  ngOnInit() {

    this.uploadForm = this.formBuilder.group({
      profile: ['']
    });
  }

  onFileSelect(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.uploadForm.get('profile').setValue(file);
    }
  }

  onSubmit() {
    const formData = new FormData();
    formData.append('file', this.uploadForm.get('profile').value)

    this.httpClient.post<any>(this.SERVER_URL, formData).subscribe(
      (res) => {
        this.response=res
        this.responseupload=this.response.message
        this.mode=2
      },

      (err) => console.log(err)
    );

  }

    goToPage() {

      this.router.navigate(['about']);
    }

}
