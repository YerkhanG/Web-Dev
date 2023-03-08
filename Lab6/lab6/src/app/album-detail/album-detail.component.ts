import { Component, OnInit } from '@angular/core';
import {Album} from "../models";
import {ActivatedRoute} from "@angular/router";
import {AlbumService} from "../album.service";

@Component({
  selector: 'app-post-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent implements OnInit {
  album: Album;
  newTitle : string;
  loaded: boolean;
  ReturnBack(){
    window.location.href = `http://localhost:4200/albums`;
  }

  constructor(private route: ActivatedRoute,
              private albumService: AlbumService) {
    this.album = {} as Album
    this.loaded = true;
    this.newTitle = "";
  }

  ngOnInit(): void {
    // let _id = this.route.snapshot.paramMap.get('id');
    // if(_id){
    //   // const id = parseInt(_id);
    //   const id = +_id;
    //   this.post = POSTS.find((x) => x.id === id) as Post;
    // }

    // this.route.paramMap.subscribe((params) => {
    //   let _id = params.get('id');
    //   if (_id){
    //     let id = +_id;
    //     this.post = POSTS.find((x) => x.id === id) as Post;
    //   }
    // });


    this.route.paramMap.subscribe((params) => {
      let _id = params.get('id');
      if (_id) {
        let id = +_id;
        this.albumService.getAlbum(id).subscribe(
          (response) => {
            this.album = response;
          })
        this.loaded = false;
        this.albumService.getAlbum(id).subscribe((album) => {
          this.album = album;
          this.loaded = true;
        })
      }
    });


  }
  saveTitle() {
    this.albumService.updateAlbumTitle(this.album.id, this.newTitle).subscribe(
      (response) => {
        this.album.title = response.title;
        this.newTitle = "";
      }
    )
  }


}
